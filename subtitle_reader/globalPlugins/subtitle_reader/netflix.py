#coding=utf-8

from .subtitle_alg import SubtitleAlg
from .object_finder import find
from .compatible import role

class Netflix(SubtitleAlg):
	def getVideoPlayer(self):
		obj = self.main.focusObject
		appName = obj.appModule.appName
		videoPlayer = find(obj, 'parent', 'role', role('dialog'))
		if not videoPlayer:
			if appName == 'firefox':
				videoPlayer = find(obj, 'parent', 'role', role('document'))
				if videoPlayer:
					videoPlayer = videoPlayer.firstChild.firstChild.next
				
			else:
				videoPlayer = find(obj, 'parent', 'class', 'watch-video--player-view')
				if videoPlayer:
					videoPlayer = videoPlayer.firstChild.next
				
			
		
		return videoPlayer
	
	def getSubtitleContainer(self):
		videoPlayer = self.main.videoPlayer
		appName = videoPlayer.appModule.appName
		return getattr(self, appName + 'GetSubtitleContainer')()
	
	def chromeGetSubtitleContainer(self):
		obj = self.main.videoPlayer
		obj = find(obj, 'firstChild', 'role', role('grouping'))
		return obj
	
	def firefoxGetSubtitleContainer(self):
		obj = self.main.videoPlayer
		obj = find(obj, 'firstChild', 'role', role('grouping'))
		return obj
	
	def getSubtitle(self):
		
		obj = self.main.subtitleContainer
		obj = obj.next
		return super(Netflix, self).getSubtitle(obj)
	
