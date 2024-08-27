# Enhanced Touch Gestures #

* аутор : Joseph Lee
* Preuzmi [stabilnu verziju][1]
* NVDA compatibility: 2018.2 to 2019.3

овај додатак вам пружа побољшане гестове за екране осетљиве на додир.

Note: this add-on requires NVDA 2018.2 or later running on a touchscreen
computer with Windows 8.1 or 10.

## команде

### доступне свуда

* дупли клик са 4 прста укључује помоћ за унос
* клик са задршком ради десни клик на објекат испод прста
* Prevlačenje sa 4 prsta desno: uključuje i isključuje touch
  tastaturu(obično je uključuje)

### објекатски мод

* повлачење са 3 прста на доле чита тренутни прозор
* повлачење са 3 прста на лево чита име објекта са фокусом
* повлачење са 3 прста на десно чита навигаторски објекат
* повлачење са 4 прста на горе пријављује наслов прозора
* повлачење са 4 прста на доле пријављује текст статусне траке

## интернет

овај мод вам омогућава навигацију по одређеним елементима тапните екран са 3
прста повлачите прст на доле да изаберете врсту елемената па са једним
прстом повлачите на десно да идете по изабраним елементима

## мод синтетизатора

у овом моду можете брзо изабрати глас ии променити јачину користите 2 прста
на десно да изаберете контролу и 2 прста на доле да је промените

## пиштање за кординате

ако сте у подешавањима миша укључили пиштања чућете их када истражујете
екран

## Touch command passthrough

An unassigned command is available to allow you to use touchscreen gestures
as though NVDA is not running. In order to use this, you need to assign a
command (via Input Gestures dialog) under Enhanced Touch Gestures category
to let you do this for up to ten seconds or toggle this manually. Then go to
NVDA menu/Preferences/Touch Interaction, then configure pause NVDA's touch
command value between 3 to 10 seconds (default is 5 seconds).

## Version 19.11

* Added input help messages for additional touch commands.

## Version 19.09

* Touch support can now be disabled from everywhere, not just from profiles
  other than normal profile.

## Version 19.07

* Internal changes to support future NVDA releases.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.08

* Compatible with NVDA 2018.3 and future versions.

## Version 18.06

* Add-on settings is now found in new multi-category NVDA Settings screen
  under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is
  required.
* Fixed compatibility issues with wxPython 4.

## Version 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel
  may cause error sounds to be heard due to changes made from this add-on.

## Version 18.03

* NVDA 2018.1 is required.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no
  longer included in this add-on.

## Version 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle
  configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is
  no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable
  touch support (available if profiles other than normal configuration is
  active).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NvDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using NVDA 2018.1 or later.

## Version 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

## Version 17.07.1

* Added an option in touch interaction dialog to manually toggle touch
  passthrough without use of a timer.
* With manual passthrough mode off, if touch passthrough is turned on before
  the passthrough duration expires, touch interaction would be enabled.

## Version 17.07

* Added a new dialog named Touch Interaction under NVDA's preferences menu
  to configure how NVDA works with touchscreens.
* After installing this version, when pressing keys on the touch keyboard,
  one must double tap the desired key. You can switch back to the old way by
  enabling touch typing from Touch Interaction dialog.
* Added a command (unassigned) to allow NVDA to ignore touch gestures for up
  to 10 seconds.
* Added an option in Touch Interaction dialog to allow NVDA to pause touch
  interaction between 3 to 10 seconds in order to perform touchscreen
  gestures directly (as though NVDA is not running; default is 5 seconds).
* Added debug logging messages when performing right clicks (tap and hold)
  to be recorded in the NVDA log (requires NVDA 2017.1 or later).
* Due to changes made when playing screen coordinates, NVDA 2017.1 or later
  is required.

##Version 17.03

* Popravljena greška kada zvučni signal za grešku nije ispravno reprodukovan
  ili se reprodukovao ton za grešku u verziji 2017.1

##verzija 16.12

* Web režim dodira radi u programima Microsoft Edge, Microsoft Word i
  ostalim programima gde se koristi režim pretraživanja
* Dodate liste i regioni u režimu pretraživanja

## Verzija 16.06

* Prva stabilna verzija

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
