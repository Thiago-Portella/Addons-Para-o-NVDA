# -*- coding: utf-8 -*-
# NVDA add-on to emulate Applications key and mouse clicks
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023/2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules
import globalPluginHandler
import addonHandler
import api
import winUser
import globalVars
from scriptHandler import script
from nvwave import playWaveFile
from threading import Thread
import wx
import os
from . import keyFunc

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(
		gesture=None,
		description= _("Emulates applications key"),
		category= _("RemapApplicationsKey"))
	def script_RunAplicationn(self, gesture):
				executeFunction(1).start()

	@script(
		gesture=None,
		description= _("Emulates shift + applications key"),
		category= _("RemapApplicationsKey"))
	def script_RunShiftAplicationn(self, gesture):
				executeFunction(2).start()

	@script(
		gesture=None,
		description= _("Emulates a mouse left click on focus"),
		category= _("RemapApplicationsKey"))
	def script_RunLeftMouse(self, gesture):
				executeFunction(3).start()

	@script(
		gesture=None,
		description= _("Emulates a mouse right click on focus"),
		category= _("RemapApplicationsKey"))
	def script_RunRightMouse(self, gesture):
				executeFunction(4).start()

class executeFunction(Thread):
	def __init__(self, opt):
		super(executeFunction, self).__init__()

		self.opt = opt
		self.daemon = True

	def run(self):
		def mouseClick(button="left"):
			if button == "left":
				winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
				winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
			if button == "right":
				winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
				winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

		def btnAplication():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			keyFunc.key_aplicacion()

		def btnShiftAplication():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			keyFunc.key_shift_aplicacion()

		def btnLeftMouse():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			mouseClick("left")
			playWaveFile(os.path.join(globalVars.appArgs.configPath, "addons", "remapApplicationsKey", "globalPlugins", "remapApplicationsKey", "sounds", "Click.wav"))

		def btnRightMouse():
			obj=api.getFocusObject()
			api.moveMouseToNVDAObject(obj)
			mouseClick("right")
			playWaveFile(os.path.join(globalVars.appArgs.configPath, "addons", "remapApplicationsKey", "globalPlugins", "remapApplicationsKey", "sounds", "Click.wav"))

		if self.opt == 1:
			wx.CallAfter(btnAplication)
		elif self.opt == 2:
			wx.CallAfter(btnShiftAplication)
		elif self.opt == 3:
			wx.CallAfter(btnLeftMouse)
		elif self.opt == 4:
			wx.CallAfter(btnRightMouse)
