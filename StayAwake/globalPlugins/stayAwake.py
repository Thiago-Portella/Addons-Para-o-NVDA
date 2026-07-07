# stayAwake.py
# NVDA Global Plugin
# StayAwake – Prevent system idle / sleep safely

import globalPluginHandler
import ui
import ctypes

# Windows execution state flags
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

kernel32 = ctypes.windll.kernel32


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """
    StayAwake NVDA add-on.
    Prevents Windows from entering idle sleep or lock state.
    """

    # This category name appears in Input Gestures
    scriptCategory = "StayAwake"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enabled = False

    # ------------------------------------------------------------
    # Toggle StayAwake
    # ------------------------------------------------------------
    def script_toggleStayAwake(self, gesture):
        """Toggle StayAwake on or off"""
        if self._enabled:
            self._disable()
        else:
            self._enable()

    def _enable(self):
        kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED
        )
        self._enabled = True
        ui.message("StayAwake enabled")

    def _disable(self):
        kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        self._enabled = False
        ui.message("StayAwake disabled")

    # ------------------------------------------------------------
    # Status-only announcement
    # ------------------------------------------------------------
    def script_stayAwakeStatus(self, gesture):
        """Announce whether StayAwake is currently enabled"""
        if self._enabled:
            ui.message("StayAwake is enabled")
        else:
            ui.message("StayAwake is disabled")

    # ------------------------------------------------------------
    # Cleanup when NVDA exits
    # ------------------------------------------------------------
    def terminate(self):
        if self._enabled:
            kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        super().terminate()

    # ------------------------------------------------------------
    # Default gestures
    # ------------------------------------------------------------
    __gestures = {
        "kb:NVDA+control+shift+a": "toggleStayAwake",
        "kb:NVDA+control+shift+i": "stayAwakeStatus",
    }
