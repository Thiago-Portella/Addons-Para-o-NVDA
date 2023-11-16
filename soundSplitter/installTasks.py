# SoundSplitter/installTasks.py
# Copyright: 2022, Joseph Lee. 2023, Luke Davis. Released under GPL V2.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import gui
	import wx
	import winVersion
	import globalVars
	# Do not present dialogs if minimal mode is set.
	# Sound Splitter requires Windows 10 21H2 or later.
	currentWinVer = winVersion.getWinVer()
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	minimumWinVer = winVersion.WIN10_21H2
	if currentWinVer < minimumWinVer:
		if not globalVars.appArgs.minimal:
			gui.messageBox(
				_(
					# Translators: Dialog text shown when trying to install the add-on on
					# releases earlier than minimum supported release.
					"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
					"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
				).format(
					releaseName=currentWinVer.releaseName,
					build=currentWinVer.build,
					supportedReleaseName=minimumWinVer.releaseName,
					supportedBuild=minimumWinVer.build
				), unsupportedWindowsReleaseTitle, wx.OK | wx.ICON_ERROR
			)
		raise RuntimeError("Attempting to install Sound Splitter on unsupported Windows release.")
