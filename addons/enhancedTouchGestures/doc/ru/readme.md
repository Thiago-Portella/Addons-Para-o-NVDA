# Enhanced Touch Gestures #

* Автор: Joseph Lee
* Загрузить [стабильную версию][1]
* NVDA compatibility: 2019.3 and beyond

Это дополнение предоставляет дополнительные жесты сенсорного экрана для
NVDA. Также, оно предоставляет набор жестов для облегчения навигации режима
обзора.

Note: this add-on requires NVDA 2019.3 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Команды

### Доступно везде

* Двойное касание четырьмя пальцами: включить режим справки по вводу.
* Касание с последующим удержанием: выполнить щелчок правой кнопки мыши на
  объекте под вашим пальцем.
* Смахивание четырьмя пальцами вправо: Изменить состояние экранной
  клавиатуры (обычно, вызывает ее)

### Объектный режим

* Смахивание тремя пальцами вниз: прочитать текущее окно.
* Смахивание тремя пальцами влево: Объявить объект в фокусе.
* Смахивание тремя пальцами вправо: Объявить текущий объект навигатора.
* Смахивание четырьмя пальцами вверх: Объявляет название текущего окна.
* смахивание четырьмя пальцами вниз: прочитать текст строки состояния.

## Сенсорный режим веб

Этот сенсорный режим, доступный в режиме обзора, позволяет осуществлять
навигацию  в документе по выбранным элементам. Чтобы переключиться в
Сенсорный режим веб из режима обзора документа, выполните двойное касание
тремя пальцами. В этом режиме пролистывания одним пальцем вверх или вниз
выбирают доступные действия с элементом, а пролистывания одним пальцем влево
или вправо перемещают к предыдущему и следующему элементам
соответственно. Когда вы покинете режим обзора документов, будет активирован
объектный режим.

## Сенсорный режим настроек синтезатора

Вы можете использовать этот режим для быстрого изменения настроек
синтезатора, таких как выбор голоса и изменения громкости. В этом режиме
используются пролистывания двумя пальцами влево или вправо, чтобы
перемещаться между настройками синтезатора и пролистывания двумя пальцами
вверх и вниз, чтобы изменить значения. Это зеркало жестов настроек
клавиатурных команд кольца синтезатора.

## Сигнал объявления координат

Если вы включили настройку изменяющегося сигнала при перемещении мыши в
настройках мыши, вы услышите звуковой сигнал, указывающий текущие координаты
экрана, когда вы используете исследование сенсорными жестами.

## Touch command passthrough

An unassigned command is available to allow you to use touchscreen gestures
as though NVDA is not running. In order to use this, you need to assign a
command (via Input Gestures dialog) under Enhanced Touch Gestures category
to let you do this for up to ten seconds or toggle this manually. Then go to
NVDA menu/Preferences/Touch Interaction, then configure pause NVDA's touch
command value between 3 to 10 seconds (default is 5 seconds).

## Version 20.01

* NVDA 2019.3 or later is required.
* Touch support toggle command (including touch passthrough) will no longer
  function if touch support is turned off completely.

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

## Версия 18.03

* Требуется NVDA 2018.1.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no
  longer included in this add-on.

## Версия 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle
  configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is
  no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable
  touch support (available if profiles other than normal configuration is
  active).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice in NVDA's preferences menu. The second item is the dialog that comes
  with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using NVDA 2018.1 or later.

## Версия 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

## Версия 17.07.1

* Added an option in touch interaction dialog to manually toggle touch
  passthrough without use of a timer.
* With manual passthrough mode off, if touch passthrough is turned on before
  the passthrough duration expires, touch interaction would be enabled.

## Версия 17.07

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

##Версия 17.03

* Fixed an issue where coordinate announcement beep did not play or an error
  tone played instead when using NVDA 2017.1 or later.

##Версия 16.12

* Сенсорный режим веб работает в Microsoft EDGE, Microsoft Word и в других
  приложениях, где используется режим просмотра.
* Добавлены списки и ориентиры для элементов режимаweb touch.

## Версия 16.06

* Первая стабильная версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
