# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2026 Joseph Lee, Kefas Lungu, released under GPL.
# Implements needed improvements for various touchscreen gestures.

from typing import NamedTuple
import globalPluginHandler
from functools import cached_property
import touchHandler
import keyboardHandler
import scriptHandler
import inputCore
import ui
from globalCommands import commands
import browseMode
import treeInterceptorHandler
import api
import config
import tones
import wx
from logHandler import log
from utils.displayString import DisplayStringStrEnum
import addonHandler

addonHandler.initTranslation()

# NVDA 2026.2: patch touchHandler.TouchMode enumeration to add synth settings mode.
class TouchMode(DisplayStringStrEnum):
	"""Available touch screen navigation modes."""

	TEXT = "text"
	OBJECT = "object"
	BROWSE = "browse"
	SYNTHSETTINGS = "synthsettings"

	@cached_property
	def _displayStringLabels(self):
		return {
			# Translators: The name of a touch mode.
			TouchMode.TEXT: _("text mode"),
			# Translators: The name of a touch mode.
			TouchMode.OBJECT: _("object mode"),
			# Translators: The name of a touch mode used when in browse mode.
			TouchMode.BROWSE: _("browse mode"),
			# Translators: The name of a touch mode.
			TouchMode.SYNTHSETTINGS: _("synth settings mode"),
		}


# Disable the add-on completely if touch support is disabled (hardware or this is portable NVDA).
def touchSupportRequired(cls):
	return globalPluginHandler.GlobalPlugin if not touchHandler.touchSupported() else cls


@touchSupportRequired
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Enhanced Touch Gestures")

	def __init__(self):
		super().__init__()
		# Notify if touch support is off.
		# This is useful if using NVDA on a shared computer.
		if not config.conf["touch"]["enabled"]:
			log.debug("etouch: touch support disabled from NVDA")
			tones.beep(380, 100)
			wx.CallAfter(ui.message, "Touch interaction support is disabled")
		# Add synth settings ring layer by patching touch handler touch mode enumeration.
		# In addition, add browse mode layer if running NVDA 2026.1 and earlier.
		# This also includes handling post browse mode state change action in NVDA 2026.1 and earlier.
		treeInterceptorHandler.post_browseModeStateChange.register(self._browseModeStateChange)
		if hasattr(touchHandler, "TouchMode"):
			touchHandler.TouchMode = TouchMode
			touchHandler.availableTouchModes = [TouchMode.TEXT, TouchMode.OBJECT, TouchMode.SYNTHSETTINGS]
		else:
			touchHandler.availableTouchModes = ["text", "object", "synthsettings"]
			touchHandler.touchModeLabels["synthsettings"] = "synth settings mode"
			touchHandler.touchModeLabels["browse"] = "browse mode"

	def terminate(self):
		super().terminate()
		# Remove the add-on from post browse mode state change notifications.
		treeInterceptorHandler.post_browseModeStateChange.unregister(self._browseModeStateChange)

	# Global commands: additional touch commands available everywhere.

	@scriptHandler.script(
		description=commands.script_toggleInputHelp.__doc__,
		gesture="ts:4finger_double_tap",
		speakOnDemand=True,
	)
	def script_toggleInputHelp(self, gesture: inputCore.InputGesture):
		commands.script_toggleInputHelp(gesture)

	@scriptHandler.script(
		description=commands.script_reportCurrentFocus.__doc__,
		gesture="ts:4finger_flickLeft",
		speakOnDemand=True,
	)
	def script_reportCurrentFocus(self, gesture: inputCore.InputGesture):
		commands.script_reportCurrentFocus(gesture)

	@scriptHandler.script(
		description=commands.script_title.__doc__,
		gesture="ts:4finger_flickUp",
		speakOnDemand=True,
	)
	def script_title(self, gesture: inputCore.InputGesture):
		commands.script_title(gesture)

	@scriptHandler.script(
		description=commands.script_reportStatusLine.__doc__,
		gesture="ts:4finger_flickDown",
		speakOnDemand=True,
	)
	def script_reportStatusLine(self, gesture: inputCore.InputGesture):
		commands.script_reportStatusLine(gesture)

	@scriptHandler.script(
		description=commands.script_speakForeground.__doc__,
		gesture="ts(object):3finger_flickDown",
		speakOnDemand=True,
	)
	def script_speakForeground(self, gesture: inputCore.InputGesture):
		commands.script_speakForeground(gesture)

	@scriptHandler.script(
		description=commands.script_navigatorObject_current.__doc__,
		gesture="ts:4finger_flickRight",
		speakOnDemand=True,
	)
	def script_navigatorObject_current(self, gesture: inputCore.InputGesture):
		commands.script_navigatorObject_current(gesture)

	# the following doesn't need speak on demand, skip it.
	# audio ducking mode, cycle speech symbol level, screen curtain toggle, and quit NVDA.

	@scriptHandler.script(
		description=commands.script_cycleAudioDuckingMode.__doc__,
		gesture="ts:4finger_tap",
	)
	def script_audioDuckingMode(self, gesture: inputCore.InputGesture):
		commands.script_cycleAudioDuckingMode(gesture)

	@scriptHandler.script(
		description=commands.script_cycleSpeechSymbolLevel.__doc__,
		gesture="ts:3finger_double_tap",
	)
	def script_speechSymbolLevel(self, gesture: inputCore.InputGesture):
		commands.script_cycleSpeechSymbolLevel(gesture)

	@scriptHandler.script(
		description=commands.script_toggleScreenCurtain.__doc__,
		gesture="ts:3finger_triple_tap",
	)
	def script_toggleScreenCurtain(self, gesture: inputCore.InputGesture):
		commands.script_toggleScreenCurtain(gesture)

	@scriptHandler.script(
		description=commands.script_quit.__doc__,
		gesture="ts:2finger_triple_tap",
	)
	def script_quitNvda(self, gesture: inputCore.InputGesture):
		commands.script_quit(gesture)

	# Web browse mode navigation:
	# Included in NVDA 2026.2

	def _browseModeStateChange(self, browseMode: bool = False) -> None:
		# Browse mode toggle is part of NVDA 2026.2.
		if hasattr(touchHandler, "TouchMode"):
			return
		if browseMode:
			if "browse" not in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.append("browse")
			touchHandler.handler._curTouchMode = "browse"
		else:
			# If we're not in browser window and web (browse) mode was active, force object mode.
			if touchHandler.handler._curTouchMode == "browse":
				touchHandler.handler._curTouchMode = "object"
			# Remove browse touch mode.
			if "browse" in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.remove("browse")

	# Web elements and associated scripts list:
	WebBrowseElement = NamedTuple(
		"WebBrowseElement", [
			("script", str),
			("element", str)
		]
	)
	webBrowseElements = (
		WebBrowseElement("", "default"),
		WebBrowseElement("Heading", "headings"),
		WebBrowseElement("Table", "tables"),
		WebBrowseElement("Link", "links"),
		WebBrowseElement("FormField", "form fields"),
		WebBrowseElement("List", "lists"),
		WebBrowseElement("Frame", "frames"),
		WebBrowseElement("Graphic", "graphics"),
		WebBrowseElement("Landmark", "landmarks"),
		WebBrowseElement("EmbeddedObject", "embedded objects"),
		WebBrowseElement("TextParagraph", "text paragraphs"),
	)
	# The starting index for the web browse mode, which flicks through objects.
	webBrowseMode = 0

	# Touch gestures please.
	# doesn't actually need touch on demand since the entire keyboard is also silenced.
	# If running on NVDA 2026.2, performs built-in browse touch mode commands.

	@scriptHandler.script(
		description="Selects the next browse mode element.",
		gesture="ts(browse):flickDown",
	)
	def script_nextBrowseModeElement(self, gesture: inputCore.InputGesture):
		if hasattr(browseMode.BrowseModeTreeInterceptor, "script_nextBrowseElement"):
			api.getFocusObject().treeInterceptor.script_nextBrowseElement(gesture)
			return
		self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode].element)
		log.debug(f"etouch: switching browse mode to {self.webBrowseElements[self.webBrowseMode]}")

	@scriptHandler.script(
		description="Selects the previous browse mode element.",
		gesture="ts(browse):flickUp",
	)
	def script_prevBrowseModeElement(self, gesture: inputCore.InputGesture):
		if hasattr(browseMode.BrowseModeTreeInterceptor, "script_prevBrowseElement"):
			api.getFocusObject().treeInterceptor.script_prevBrowseElement(gesture)
			return
		self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode].element)
		log.debug(f"etouch: switching browse mode to {self.webBrowseElements[self.webBrowseMode]}")

	@scriptHandler.script(gesture="ts(browse):flickRight")
	def script_nextSelectedElement(self, gesture: inputCore.InputGesture):
		if hasattr(browseMode.BrowseModeTreeInterceptor, "script_nextSelectedElement"):
			api.getFocusObject().treeInterceptor.script_nextSelectedElement(gesture)
			return
		if (
			isinstance(
				(obj := api.getNavigatorObject().treeInterceptor),
				browseMode.BrowseModeTreeInterceptor
			) and self.webBrowseMode > 0  # An actual browse mode element
		):
			getattr(
				obj,
				f"script_next{self.webBrowseElements[self.webBrowseMode].script}"
			)(gesture)
		else:
			commands.script_navigatorObject_nextInFlow(gesture)

	@scriptHandler.script(gesture="ts(browse):flickLeft")
	def script_prevSelectedElement(self, gesture: inputCore.InputGesture):
		if hasattr(browseMode.BrowseModeTreeInterceptor, "script_prevSelectedElement"):
			api.getFocusObject().treeInterceptor.script_prevSelectedElement(gesture)
			return
		if (
			isinstance(
				(obj := api.getNavigatorObject().treeInterceptor),
				browseMode.BrowseModeTreeInterceptor
		) and self.webBrowseMode > 0  # An actual browse mode element
		):
			getattr(
				obj,
				f"script_previous{self.webBrowseElements[self.webBrowseMode].script}"
			)(gesture)
		else:
			commands.script_navigatorObject_previousInFlow(gesture)

	# Press Tab and Shift+Tab.

	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Emulates pressing tab on the system keyboard"),
		gesture="ts:3finger_flickRight",
	)
	def script_pressTab(self, gesture: inputCore.InputGesture):
		keyboardHandler.KeyboardInputGesture.fromName("tab").send()

	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Emulates pressing shift+tab on the system keyboard"),
		gesture="ts:3finger_flickLeft",
	)
	def script_pressShiftTab(self, gesture: inputCore.InputGesture):
		keyboardHandler.KeyboardInputGesture.fromName("shift+tab").send()

	# Synth settings ring/mode

	@scriptHandler.script(
		description=commands.script_increaseSynthSetting.__doc__,
		gesture="ts(synthsettings):2finger_flickUp",
		speakOnDemand=True,
	)
	def script_prevSynthSettingValue(self, gesture: inputCore.InputGesture):
		commands.script_increaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_decreaseSynthSetting.__doc__,
		gesture="ts(synthsettings):2finger_flickDown",
		speakOnDemand=True,
	)
	def script_nextSynthSettingValue(self, gesture: inputCore.InputGesture):
		commands.script_decreaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_nextSynthSetting.__doc__,
		gesture="ts(synthsettings):2finger_flickRight",
		speakOnDemand=True,
	)
	def script_nextSynthSetting(self, gesture: inputCore.InputGesture):
		commands.script_nextSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_previousSynthSetting.__doc__,
		gesture="ts(synthsettings):2finger_flickLeft",
		speakOnDemand=True,
	)
	def script_prevSynthSetting(self, gesture: inputCore.InputGesture):
		commands.script_previousSynthSetting(gesture)
