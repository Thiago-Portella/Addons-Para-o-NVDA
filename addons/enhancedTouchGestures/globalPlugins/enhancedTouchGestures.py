# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2024 Joseph Lee, Kefas Lungu, released under GPL.
# Implements needed improvements for various touchscreen gestures.

import globalPluginHandler
import touchHandler
import scriptHandler
import ui
from globalCommands import commands, GlobalCommands
import browseMode
import extensionPoints
import api
import winUser
import config
import windowUtils
import tones
import versionInfo
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
import wx
from logHandler import log
import addonHandler
addonHandler.initTranslation()

# Support speak on demand mode: NVDA 2024.1 or later
speakOnDemandMode = {"speakOnDemand": True} if versionInfo.version_year >= 2024 else {}
# Notifies when browse mode state has changed, to enter or exit web mode.
post_browseModeStateChange = extensionPoints.Action()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Enhanced Touch Gestures")
	# Set up the touch environment for the add-on.
	origAvailTouchModes = len(touchHandler.availableTouchModes) + 1

	def __init__(self):
		super().__init__()
		if not touchHandler.touchSupported():
			return
		# Notify if touch support is off.
		# This is useful if using NVDA on a shared computer.
		if not config.conf["touch"]["enabled"]:
			log.debug("etouch: touch support disabled from NVDA")
			tones.beep(380, 100)
			wx.CallAfter(ui.message, "Touch interaction support is disabled")
		# Synth settings ring layer.
		touchHandler.availableTouchModes.append("SynthSettings")
		touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
		touchHandler.touchModeLabels["web"] = "web mode"

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj, nextHandler):
		# Crucial: Don't do anything unless if it is an installed copy and touchscreen support is active.
		if config.isInstalledCopy() and touchHandler.handler:
			# From 2015 onwards, browse mode module is used.
			if (
				isinstance(obj.treeInterceptor, browseMode.BrowseModeTreeInterceptor)
				and "Web" not in touchHandler.availableTouchModes
			):
				touchHandler.availableTouchModes.append("Web")
				# automatically switch to web mode if any brows mode window is active
				touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[3]
			else:
				# If we're not in browser window, force object mode.
				if "Web" not in touchHandler.availableTouchModes:
					touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
				else:
					curAvailTouchModes = len(touchHandler.availableTouchModes)
					# If we have too many touch modes, pop all except the original entries.
					if curAvailTouchModes > self.origAvailTouchModes:
						for i in range(0, curAvailTouchModes - self.origAvailTouchModes):
							touchHandler.availableTouchModes.pop()
		nextHandler()

	# Global commands: additional touch commands available everywhere.

	@scriptHandler.script(
		description=commands.script_toggleInputHelp.__doc__,
		gesture="ts:4finger_double_tap",
		**speakOnDemandMode
	)
	def script_toggleInputHelp(self, gesture):
		commands.script_toggleInputHelp(gesture)

	@scriptHandler.script(
		description=commands.script_reportCurrentFocus.__doc__,
		gesture="ts:3finger_flickLeft",
		**speakOnDemandMode
	)
	def script_reportCurrentFocus(self, gesture):
		commands.script_reportCurrentFocus(gesture)

	@scriptHandler.script(
		description=commands.script_title.__doc__,
		gesture="ts:4finger_flickUp",
		**speakOnDemandMode
	)
	def script_title(self, gesture):
		commands.script_title(gesture)

	@scriptHandler.script(
		description=commands.script_reportStatusLine.__doc__,
		gesture="ts:4finger_flickDown",
		**speakOnDemandMode
	)
	def script_reportStatusLine(self, gesture):
		commands.script_reportStatusLine(gesture)

	@scriptHandler.script(
		description=commands.script_speakForeground.__doc__,
		gesture="ts:3finger_flickDown",
		**speakOnDemandMode
	)
	def script_speakForeground(self, gesture):
		commands.script_speakForeground(gesture)

	@scriptHandler.script(
		description=commands.script_navigatorObject_current.__doc__,
		gesture="ts:3finger_flickRight",
		**speakOnDemandMode
	)
	def script_navigatorObject_current(self, gesture):
		commands.script_navigatorObject_current(gesture)

	# the following doesn't need speak on demand, skip it.
	# audio ducking mode, cycle speech symbol level, progress bar output and quit NVDA.

	@scriptHandler.script(
		description=commands.script_cycleAudioDuckingMode.__doc__,
		gesture="ts:4finger_tap",
	)
	def script_audioDuckingMode(self, gesture):
		commands.script_cycleAudioDuckingMode(gesture)

	@scriptHandler.script(
		description=commands.script_cycleSpeechSymbolLevel.__doc__,
		gesture="ts:3finger_double_tap",
	)
	def script_speechSymbolLevel(self, gesture):
		commands.script_cycleSpeechSymbolLevel(gesture)

	@scriptHandler.script(
		description=GlobalCommands.script_toggleProgressBarOutput.__doc__,
		gesture="ts:tripple_tap",
	)
	def script_progressBarOutput(self, gesture):
		GlobalCommands.script_toggleProgressBarOutput(self, gesture)

	@scriptHandler.script(
		description=GlobalCommands.script_quit.__doc__,
		gesture="ts:2finger_tripple_tap"
	)
	def script_quitNvda(self, gesture):
		GlobalCommands.script_quit(self, gesture)

	# Web navigation:

	# Web elements list:
	webBrowseElements = (
		"Default",
		"Links",
		"Buttons",
		"Form fields",
		"Headings",
		"Frames",
		"Tables",
		"Lists",
		"Graphics",
		"Landmarks"
	)
	# The starting index for the web browse mode, which flicks through objects.
	webBrowseMode = 0

	# Touch gestures please.
	# doesn't actually need touch on demand since the entire keyboard is also silenced.

	@scriptHandler.script(
		description="Selects the next web navigation element.",
		gesture="ts(Web):flickDown"
	)
	def script_nextWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		log.debug(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	@scriptHandler.script(
		description="Selects the previous web navigation element.",
		gesture="ts(Web):flickUp"
	)
	def script_prevWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		log.debug(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands = (
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLink,
			browseMode.BrowseModeTreeInterceptor.script_previousLink
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextButton,
			browseMode.BrowseModeTreeInterceptor.script_previousButton
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFormField,
			browseMode.BrowseModeTreeInterceptor.script_previousFormField
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextHeading,
			browseMode.BrowseModeTreeInterceptor.script_previousHeading
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFrame,
			browseMode.BrowseModeTreeInterceptor.script_previousFrame
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextTable,
			browseMode.BrowseModeTreeInterceptor.script_previousTable
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextList,
			browseMode.BrowseModeTreeInterceptor.script_previousList
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextGraphic,
			browseMode.BrowseModeTreeInterceptor.script_previousGraphic
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLandmark,
			browseMode.BrowseModeTreeInterceptor.script_previousLandmark
		),
	)

	@scriptHandler.script(gesture="ts(Web):flickRight")
	def script_nextSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0:
				commands.script_navigatorObject_nextInFlow(gesture)
			else:
				self.browseModeCommands[self.webBrowseMode - 1][0](obj, gesture)

	@scriptHandler.script(gesture="ts(Web):flickLeft")
	def script_prevSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0:
				commands.script_navigatorObject_previousInFlow(gesture)
			else:
				self.browseModeCommands[self.webBrowseMode - 1][1](obj, gesture)

# toggles touch keyboard
	# again, no speak on demand is needed since touch keyboard too will also be silenced during speech on demand.
	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Toggles touch keyboard"),
		gesture="ts:4finger_flickRight"
	)
	def script_touchKeyboardEnable(self, gesture):
		# Locate the touch keyboard button and activate it, simulating JAWS 17 gesture.
		keyboardButtonHwnd = windowUtils.findDescendantWindow(
			api.getDesktopObject().windowHandle, className="TIPBand"
		)
		touchKeyboardButton = getNVDAObjectFromEvent(keyboardButtonHwnd, winUser.OBJID_CLIENT, 0)
		try:
			touchKeyboardButton.doAction()
			tones.beep(1000, 150)
		except NotImplementedError:
			# Translators: message shown when touch keyboard button is not found.
			ui.message(_("Cannot activate touch keyboard"))

	# toggles voice dectation.
	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Toggles voice dictation"),
		gesture="ts:4finger_flickLeft",
		**speakOnDemandMode
	)
	def script_win10Dictation(self, gesture):
		# Press Windows+H on Windows 10 Version 1709 (Fall Creators Update) and later.
		import winVersion
		import keyboardHandler
		if winVersion.getWinVer() < winVersion.WIN10_1709:
			# Translators: message shown when dictation command is unavailable.
			ui.message(_("Dictation is supported on Windows 10 Version 1709 or later"))
		else:
			keyboardHandler.KeyboardInputGesture.fromName("windows+h").send()

	@scriptHandler.script(
		description=commands.script_increaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickUp",
		**speakOnDemandMode
	)
	def script_prevSynthSettingValue(self, gesture):
		commands.script_increaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_decreaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickDown",
		**speakOnDemandMode
	)
	def script_nextSynthSettingValue(self, gesture):
		commands.script_decreaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_nextSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickRight",
		**speakOnDemandMode
	)
	def script_nextSynthSetting(self, gesture):
		commands.script_nextSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_previousSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickLeft",
		**speakOnDemandMode
	)
	def script_prevSynthSetting(self, gesture):
		commands.script_previousSynthSetting(gesture)
