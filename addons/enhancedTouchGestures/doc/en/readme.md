# Enhanced Touchscreen Gestures #

* Authors: Joseph Lee, Kefas Lungu
* Download [stable version][1]
* NVDA compatibility: 2024.1 and later

This add-on provides additional touchscreen gestures for NVDA. It also provides a set of gestures for easier browse mode navigation.

Note: this add-on requires NVDA 2024.1 or later running on a touchscreen computer with Windows 10 or 11.

## Commands

### Available everywhere

* 4 finger double tap: toggle input help mode.
* Four finger flick right: toggle touch keyboard (usually enables it).
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version 1709 or later).
* 4 finger flick up: report title of the current window.
* 4 finger flick down: report status bar text.
* 3 finger flick down: read current window.
* 3 finger flick left: report object with focus.
* 3 finger flick right: report current navigator object.
* 3 finger double tap: Cycles through speech symbol levels which determine what symbols are spoken
* 2 finger tripple tap: Quit NVDA!.
* 4 finger tap: Cycles through audio ducking modes.
* Triple tap: Toggles between beeps, speech, beeps and speech, and off.

## Web touch mode

This touch mode, available in browse mode, allows you to navigate the document by selected element. To switch to web mode, from browse mode documents, perform 3 finger tap. From this mode, flicking up or down with one finger cycles through available element navigation modes, while flicking right or left with one finger moves to next or previous chosen element, respectively. Once you move away from browse mode documents, object touch mode is used.
Available web modes are: Default, Links, Buttons, Form fields, Headings, Frames, Tables, Lists, Graphics, and Landmarks.
## Synth settings touch mode

You can use this mode to quickly change synthesizer settings such as choosing a voice and changing volume. In this mode, use two finger flick left or right to move between synth settings and use two finger flick up and down gestures to change values. This gestures mirrors that of synth settings ring commands on the keyboard.

## Version 23.06.1
* audio docking moved to 4 finger tap because of conflict with speech stops NVDA core command.

## Version 23.06
* Enhanced Touch gestures nvda-addon is now maintained by Kefas Lungu.
* All gestures in object mode are now available everywhere.
* New gestures are now available.
  * 3 finger double tap: Cycles through speech symbol levels which determine what symbols are spoken
  * 2 finger tripple tap: Quit NVDA!.
  * 4 finger tap: Cycles through audio ducking modes.
  * Triple tap: Toggles between beeps, speech, beeps and speech, and off.
* In web mode, it is now possible to Use buttons, graphics, and landmarks in addition to the already available browse element list.
* In web mode, NVDA is no longer going to say normal, but default when you switch to default navigation from other browse element list. For example, when switching from buttons, NVDA will now say default.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 8.1 is no longer supported by Microsoft as of January 2023.
* It is possible to reassign touch keyboard and dictation toggle commands from input gestures dialog under Enhanced Touch Gestures category.
* Removed read-only state workaround for touch keyboard keys as it is resolved in Windows 10.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.

## Version 21.08

* Initial support for Windows 11.

## Version 21.01

* NVDA 2020.3 or later is required.
* On Windows 10 Version 1709 and later, doing a four finger flick left will toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction settings panel, a dedicated Enhanced Touch Gestures settings panel has been removed.

## Version 20.09

* Removed ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough).
* Removed coordinate announcement beep feature.

## Version 20.07

* Added a keyboard command to toggle touch interaction or enable/disable touch passthrough (Control+Alt+NVDA+T).
* As NVDA 2020.1 and later includes a touch command to perform right mouse click (one finger tap and hold), the command has been removed from this add-on. AS a result, NVDA 2020.1 or later is required.
* The ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough) is deprecated. In the future this feature will toggle touch interaction instead.
* In NVDA development snapshots, due to touch interaction feature changes, touch command passthrough feature and Enhanced Touch Gestures settings panel will be disabled. The command used to enable touch command passthrough will toggle touch interaction instead.
* Coordinate announcement beep feature is deprecated and will be removed in a future add-on release.
* Coordinate announcement beep will not be heard while using touch keyboard.
* NVDA will no longer appear to do nothing or play error tones while exploring modern input facility such as emoji panel via touch.
* NVDA will present an error message if touch keyboard cannot be activated (four finger flick right).

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Right mouse click gesture (one finger tap and hold) is now part of NVDA 2020.1.

## Version 20.01

* NVDA 2019.3 or later is required.
* Touch support toggle command (including touch passthrough) will no longer function if touch support is turned off completely.

## Version 19.11

* Added input help messages for additional touch commands.

## Version 19.09

* Touch support can now be disabled from everywhere, not just from profiles other than normal profile.

## Version 19.07

* Internal changes to support future NVDA releases.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.08

* Compatible with NVDA 2018.3 and future versions.

## Version 18.06

* Add-on settings is now found in new multi-category NVDA Settings screen under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is required.
* Fixed compatibility issues with wxPython 4.

## Version 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel may cause error sounds to be heard due to changes made from this add-on.

## Version 18.03

* NVDA 2018.1 is required.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no longer included in this add-on.

## Version 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable touch support (available if profiles other than normal configuration is active).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed twice under NVDA's preferences menu. The second item is the dialog that comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer shown if using NVDA 2018.1 or later.

## Version 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA 2017.4 development snapshots.

## Version 17.07.1

* Added an option in touch interaction dialog to manually toggle touch passthrough without use of a timer.
* With manual passthrough mode off, if touch passthrough is turned on before the passthrough duration expires, touch interaction would be enabled.

## Version 17.07

* Added a new dialog named Touch Interaction under NVDA's preferences menu to configure how NVDA works with touchscreens.
* After installing this version, when pressing keys on the touch keyboard, one must double tap the desired key. You can switch back to the old way by enabling touch typing from Touch Interaction dialog.
* Added a command (unassigned) to allow NVDA to ignore touch gestures for up to 10 seconds.
* Added an option in Touch Interaction dialog to allow NVDA to pause touch interaction between 3 to 10 seconds in order to perform touchscreen gestures directly (as though NVDA is not running; default is 5 seconds).
* Added debug logging messages when performing right clicks (tap and hold) to be recorded in the NVDA log (requires NVDA 2017.1 or later).
* Due to changes made when playing screen coordinates, NVDA 2017.1 or later is required.

##Version 17.03

* Fixed an issue where coordinate announcement beep did not play or an error tone played instead when using NVDA 2017.1 or later.

##Version 16.12

* Web touch mode works in Microsoft Edge, Microsoft Word and others where browse mode is used.
* Added lists and landmarks to web touch mode elements.

## Version 16.06

* Initial stable version.

[1]: https://addons.nvda-project.org/files/get.php?file=ets
