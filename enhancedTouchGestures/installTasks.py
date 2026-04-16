# Enhanced Touch Gestures/installTasks.py
# Copyright 2017-2026 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import ctypes
import config
import gui

addonHandler.initTranslation()


def onInstall() -> None:
	# Touch support must be present, otherwise the add-on will be disabled upon installation.
	isInstalledCopy = config.isInstalledCopy()
	touchHardwarePresent = ctypes.windll.user32.GetSystemMetrics(95) > 0  # SM_MAXIMUMTOUCHES
	if isInstalledCopy and touchHardwarePresent:
		return
	# Translators: dialog title shown when trying to install the add-on on unsupported systems.
	installWarning = _("Enhanced Touch Gestures install warning")
	installMessage = None
	match (touchHardwarePresent, isInstalledCopy):
		case (False, _):  # No touch hardware whatsoever
			installMessage = _( # Translators: dialog text shown when trying to install the add-on on unsupported systems.
				"This device does not support touch interaction. A touch capable device is required to use add-on features."
			)
		case (True, False):  # Portable NVDA running on a touch capable hardware
			installMessage = _( # Translators: dialog text shown when trying to install the add-on on unsupported systems.
				"You are using a portable copy of NVDA and the device supports touch interaction. NVDA must be installed to use add-on features."
			)
		case _:
			pass
	gui.MessageDialog.alert(installMessage, installWarning)
