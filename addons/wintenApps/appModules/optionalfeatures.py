# Control Panel/Optional Features
# Copyright 2024 Joseph Lee, released under GPL

# Workarounds for Optional Features in Windows 11 canary channel builds (27000 series)

import appModuleHandler
import winUser
from winAPI.types import HWNDValT
import winVersion


class AppModule(appModuleHandler.AppModule):

	def isGoodUIAWindow(self, hwnd: HWNDValT) -> bool:
		# Workarounds for build 27000 series optional features treeview
		# IAccessible only exposes checkbox role - no name, no state changes, no mouse movement responses.
		# Thankfully, reclassifying it as UIA partly solves the problem (no stae change, however).
		if winUser.getClassName(hwnd) == "SysTreeView32" and winVersion.getWinVer().build >= 27686:
			return True
		return False
