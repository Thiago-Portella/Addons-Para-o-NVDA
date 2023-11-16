#coding=utf-8

# 字幕閱讀器
# 作者：福恩 <maxe@mail.batol.net>


import re
import ui
import time

import addonHandler
addonHandler.initTranslation()

from globalPluginHandler import GlobalPlugin
from globalVars import appArgs
from logHandler import log
from . import sound
from . import gui
from .config import conf
from .youtube import Youtube
from .maru_maru import MaruMaru
from .disney_plus import DisneyPlus
from .netflix import Netflix
from .wkMediaCommons import WKMediaCommons
from .kktv import Kktv
from .bilibili import Bilibili
from .update import Update

nvdaGui = gui.gui


wx = gui.wx

conf.load(appArgs.configPath + r'\subtitle_reader.json')

class GlobalPlugin(GlobalPlugin):
	# Translators: Script category for Subtitle Reader
	scriptCategory = _(u'字幕閱讀器')
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.subtitleAlgs = {
			'.+ - YouTube': Youtube(self, onFoundSubtitle=self.processSubtitle),
			'.+-MARUMARU': MaruMaru(self),
			'^Disney\+ \| ': DisneyPlus(self),
			'.*?Netflix': Netflix(self),
			'.+ - Wikimedia Commons': WKMediaCommons(self),
			'.+ \| KKTV': Kktv(self),
			'.+_哔哩哔哩_bilibili': Bilibili(self),
		}
		self.subtitleAlg = None
		self.supportedBrowserAppNames = ('chrome', 'brave', 'firefox', 'msedge')
		self.focusObject = None
		self.videoPlayer = None
		self.subtitleContainer = None
		self.subtitle = str()
		self.emptySubtitleTime = 0
		# 使用 wx.PyTimer 不斷執行函數
		self.readSubtitleTimer = nvdaGui.NonReEntrantTimer(self.readSubtitle)
		self.startReadSubtitleTime = 0
		
		sound.init()
		
		self.update = Update()
		# 初始化選單
		self.initMenu()
	
	def initMenu(self):
		menu = self.menu = gui.Menu()
		gui.tray.Bind(gui.wx.EVT_MENU, self.script_toggleSwitch, menu.switch)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleBackgroundReading, menu.backgroundReading)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleReadChat, menu.readChat)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleReadChatSender, menu.readChatSender)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleReadChatGiftSponser, menu.readChatGiftSponser)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleOmitChatGraphic, menu.omitChatGraphic)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleInfoCardPrompt, menu.infoCardPrompt)
		gui.tray.Bind(gui.wx.EVT_MENU, self.toggleReadChapter, menu.readChapter)
		gui.tray.Bind(gui.wx.EVT_MENU, self.update.manualCheck, menu.checkForUpdate)
		gui.tray.Bind(gui.wx.EVT_MENU, self.update.openChangeLog, menu.openChangeLog)
		gui.tray.Bind(gui.wx.EVT_MENU, self.update.toggleCheckAutomatic, menu.checkUpdateAutomatic)
		menu.switch.Check(conf['switch'])
		menu.backgroundReading.Check(conf['backgroundReading'])
		menu.readChat.Check(conf['readChat'])
		menu.readChatSender.Check(conf['readChatSender'])
		menu.readChatGiftSponser.Check(conf['readChatGiftSponser'])
		menu.omitChatGraphic.Check(conf['omitChatGraphic'])
		menu.infoCardPrompt.Check(conf['infoCardPrompt'])
		menu.readChapter.Check(conf['readChapter'])
		menu.checkUpdateAutomatic.Check(conf['checkUpdateAutomatic'])
	
	def terminate(self):
		# 關閉 NVDA 時，儲存開關狀態到使用者設定檔。
		conf.write()
		gui.toolsMenu.DestroyItem(self.menu.menuItem.Id)
		
		sound.free()
	
	def startReadSubtitle(self):
		self.readSubtitleTimer.Start(0, wx.TIMER_CONTINUOUS)
	
	def stopReadSubtitle(self):
		self.readSubtitleTimer.Stop()
	
	def script_toggleSwitch(self, gesture):
		switch = conf['switch'] = not conf['switch']
		if switch:
			self.executeSubtitleAlg()
			# Translators: This will be displayed when the reader switch is turned on
			ui.message(_(u'開始閱讀字幕'))
		else:
			self.stopReadSubtitle()
			# Translators: This will be displayed when the reader switch is turned off
			ui.message(_(u'停止閱讀字幕'))
		
		self.menu.switch.Check(switch)
	
	# Translators: Reader's toggle switch
	script_toggleSwitch.__doc__ = _(u'閱讀器開關')
	
	def event_gainFocus(self, obj, call_to_skip_event):
		'''
		取得新焦點時，重新取得字幕演算法。
		'''
		call_to_skip_event()
		
		self.focusObject = obj
		self.executeSubtitleAlg()
	
	def executeSubtitleAlg(self):
		obj = self.focusObject
		if obj.role == 0:
			# 嵌入的 Youtube 頁框，在開始播放約 5 秒之後，會將焦點拉到一個不明的物件上，且 NVDA 無法查看其相鄰的物件，故將他跳過。
			return
		
		if not conf['backgroundReading']:
			self.stopReadSubtitle()
			self.videoPlayer = None
		
		if not conf['switch']:
			return
		
		if obj.appModule.appName not in self.supportedBrowserAppNames:
			return
		
		alg = self.getSubtitleAlg()
		if not alg:
			return
		
		self.subtitleAlg = alg
		
		videoPlayer = self.videoPlayer = alg.getVideoPlayer()
		if not videoPlayer:
			return
		
		container = self.subtitleContainer = alg.getSubtitleContainer()
		if not container:
			return
		
		self.startReadSubtitle()
	
	def getSubtitleAlg(self):
		window = self.focusObject.objectInForeground().name
		for alg in self.subtitleAlgs:
			if re.match(alg, window):
				return self.subtitleAlgs[alg]
			
		
	
	def readSubtitle(self):
		'''
		尋找並閱讀字幕，必須不斷執行。
		'''
		if not conf['switch'] or not self.subtitleContainer:
			return
		
		if not self.videoPlayer or not self.videoPlayer.role:
			return
		
		elapsedTime = time.time() - self.startReadSubtitleTime
		if elapsedTime < 0.1:
			return
		
		self.startReadSubtitleTime = time.time()
		subtitle = self.subtitleAlg.getSubtitle()
		if subtitle is None:
			return
		
		self.processSubtitle(subtitle)
	
	def processSubtitle(self, subtitle):
		# 刪除用於渲染字幕效果的符號
		subtitle = subtitle.replace(u'​', '').replace(u' ', '')
		log.debug('original subtitle = ' + subtitle)
		subtitle = self.filterSamePart(subtitle)
		
		if not subtitle:
			# 沒有字幕超過一秒鐘才清除字幕緩衝區。
			if not self.emptySubtitleTime:
				self.emptySubtitleTime = time.time()
			elif time.time() - self.emptySubtitleTime >= 1:
				self.subtitle = ''
			
			return
		
		self.emptySubtitleTime = 0
		
		if subtitle == self.subtitle:
			return
		
		lastSubtitle = self.subtitle
		lastSubtitleText = lastSubtitle.replace(' | ', '')
		subtitleText = subtitle.replace(' | ', '')
		self.subtitle = subtitle
		
		msg = subtitleText
		
		# 若新的字幕內容是前一字幕的一部分，則不報讀。
		if subtitleText in lastSubtitleText:
			msg = ''
		
		# 若新的字幕包含前一字幕的內容，則只報讀填充的部分。
		if lastSubtitleText and lastSubtitleText in subtitleText:
			msg = subtitleText.replace(lastSubtitleText, '', 1)
		
		# 使用分隔符號來忽略兩次字幕之間相同的內容
		split = subtitle.split(' | ')
		for part in split:
			part = part.replace(' | ', '')
			if part in lastSubtitleText:
				msg = msg.replace(part, '')
			
		
		log.debug('subtitle = ' + subtitle)
		log.debug('last subtitle = ' + lastSubtitle)
		log.debug('msg = ' + msg)
		
		if not msg:
			msg = None
		
		ui.message(msg)
	
	def filterSamePart(self, subtitle):
		parts = subtitle.split(' | ')
		newParts = []
		for part in parts:
			if any(s for s in newParts if part.strip() in s.strip() or part.strip() == s.strip()):
				continue
			
			matchPart = [s for s in newParts if s.strip() in part.strip()]
			if matchPart:
				newParts.remove(matchPart[0])
			
			newParts.append(part)
		
		return ' | '.join(newParts)
	
	def toggleBackgroundReading(self, evt):
		conf['backgroundReading'] = not conf['backgroundReading']
		self.menu.backgroundReading.Check(conf['backgroundReading'])
	
	def toggleReadChat(self, evt):
		conf['readChat'] = not conf['readChat']
		self.menu.readChat.Check(conf['readChat'])
	
	def toggleReadChatSender(self, evt):
		conf['readChatSender'] = not conf['readChatSender']
		self.menu.readChatSender.Check(conf['readChatSender'])
	
	def toggleReadChatGiftSponser(self, evt):
		conf['readChatGiftSponser'] = not conf['readChatGiftSponser']
		self.menu.readChatGiftSponser.Check(conf['readChatGiftSponser'])
	
	def toggleOmitChatGraphic(self, evt):
		conf['omitChatGraphic'] = not conf['omitChatGraphic']
		self.menu.omitChatGraphic.Check(conf['omitChatGraphic'])
	
	def toggleInfoCardPrompt(self, evt):
		conf['infoCardPrompt'] = not conf['infoCardPrompt']
		self.menu.infoCardPrompt.Check(conf['infoCardPrompt'])
	
	def toggleReadChapter(self, evt):
		conf['readChapter'] = not conf['readChapter']
		self.menu.readChapter.Check(conf['readChapter'])
	
	__gestures = {
		'kb:nvda+y': 'toggleSwitch',
	}
