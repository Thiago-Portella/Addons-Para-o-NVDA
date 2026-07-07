# Enhanced Touchscreen Gestures

* Authors: Joseph Lee, Kefas Lungu

This add-on provides additional touchscreen gestures for NVDA. It also provides a set of gestures for easier browse mode navigation.

Note: this add-on requires NVDA 2025.3.3 or later running on a touchscreen computer with Windows 10 or 11.

## Commands

### Available everywhere

* Two finger tripple tap: quits NVDA!
* Three finger flick right: press Tab.
* Three finger flick left: press Shift+Tab.
* Three finger flick down (object mode): read current window.
* Three finger double tap: cycles through speech symbol levels which determine what symbols are spoken.
* Three finger triple tap: toggles screen curtain.
* Four finger tap: cycles through audio ducking modes.
* Four finger double tap: toggle input help mode.
* Four finger flick left: report object with focus.
* Four finger flick right: report current navigator object.
* Four finger flick up: report title of the current window.
* Four finger flick down: report status bar text.

## Touch browse mode

This touch mode, available in browse mode, allows you to navigate the document by selected element. This mode is entered automatically when browse mode becomes active, including switching to a browse mode document. From this mode, flicking up or down with one finger cycles through available element navigation modes, while flicking right or left with one finger moves to next or previous chosen element, respectively. Once you move away from browse mode documents or switch to focus mode, object touch mode will be used.

Available touch browse mode elements can vary between NVDA versionns. For NVDA 2025.3.3 and 2026.1, the available elements are default (move through elements/objects regardless of type), headings, tables, links, form fields, lists, frames, graphics, landmarks, embedded objects (dialogs and web apps, for example), and text paragraphs. In NVDA 2026.2, the available elements by default are default, headings, tables, links, form fields, and lists, with additional elements selectable from browse mode NVDA settings category.

Note: this feature is included in NVDA 2026.2.

## Synth settings touch mode

You can use this mode to quickly change synthesizer settings such as choosing a voice and changing volume. In this mode, use two finger flick left or right to move between synth settings and use two finger flick up and down gestures to change values. This gestures mirrors that of synth settings ring commands on the keyboard.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/enhancedTouchGestures/blob/main/changes.md
