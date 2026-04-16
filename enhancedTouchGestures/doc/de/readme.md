# Erweiterte Touch-Gesten #

* Autor: Joseph Lee

Diese Erweiterung führt zusätzliche Touchscreen-Gesten in NVDA ein. Neue
Touchscreen-Gesten für den Lesemodus sind ebenfalls verfügbar.

Note: this add-on requires NVDA 2024.1 or later running on a touchscreen
computer with Windows 10 or 11.

## Befehle

### Überall verfügbar

* Mit vier Fingern zweimal tippen: Eingabehilfe ein-/ausschalten.
* Mit vier Fingern nach rechts streichen: Aktiviert die Bildschirmtastatur.
* Mit vier Fingern nach links wischen: Diktat umschalten (Windows+H; Windows
  10 Version 1709 oder neuer).

### Objektmodus

* Mit drei Fingern nach unten streichen: Aktuelles Fenster vorlesen.
* Mit drei Fingern nach links streichen: Fukussiertes Objekt ausgeben.
* Mit drei Fingern nach rechts streichen: Aktuelles Navigator-Objekt
  ausgeben.
* Mit vier Fingern nach oben streichen: Titelleiste ansagen.
* Mit vier Fingern nach unten streichen: Statusleiste ansagen.

## Web-Touch-Modus

In diesem Modus können Sie Elementtypen im Lesemodus auswählen und zwischen
Elementen des ausgewählten Elementtyps navigieren. Um in den Webmodus zu
wechseln, tippen Sie aus dem Lesemodus mit 3 Fingern auf dem Bildschirm. Von
diesem Modus aus können Sie mit einem Finger nach oben oder unten durch die
verfügbaren Elementtypen blättern, während Sie mit einem Finger nach rechts
oder links zum nächsten bzw. vorherigen Element des ausgewählten Elementtyps
gelangen. Sobald Sie das Dokument im Lesemodus beenden bzw. zu einem anderen
Fenster wechseln, wo der Lesemodus deaktiviert oder nicht verfügbar ist,
wird automatisch die Objektnavigation aktiviert.

## Modus für Sprachausgabeneinstellungen

In diesem Modus können Sie Sprachausgabeneinstellungen wie Tonhöhe,
Geschwindigkeit oder Lautstärke ändern. Um zwischen den einstellungen zu
wechseln, streichen Sie mit 2 Fingern nach links oder rechts. Um eine
Einstellung zu ändern, streichen Sie mit 2 Fingern nach oben oder
unten. Diese Gesten ähneln den Tastenkombinationen für Einstellungen im
Einstellungsring (STRG+Umschalt+NVDA+Pfeiltasten).

## Version 25.07

* Made the add-on code more robust with help from Pyright (a Python static
  type checker).

## Version 25.02

* Restored limited support for Windows 8.1.

## Version 25.01

* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.

## Version 24.05

* NVDA 2024.1 or later is required.

## Version 23.06.1

* audio ducking moved to 4 finger tap due to conflict with speech stops NVDA
  command.

## Version 23.06

* Enhanced Touch gestures nvda-addon is now maintained by Kefas Lungu.
* All gestures in object mode are now available everywhere.
* New gestures are now available.

  * 3 finger double tap: Cycles through speech symbol levels which determine
    what symbols are spoken
  * 2 finger tripple tap: Quit NVDA!.
  * 4 finger tap: Cycles through audio ducking modes.
  * Triple tap: Toggles between beeps, speech, beeps and speech, and off.

* In web mode, it is now possible to Use buttons, graphics, and landmarks in
  addition to the already available browse element list.
* In web mode, NVDA is no longer going to say normal, but default when you
  switch to default navigation from other browse element list. For example,
  when switching from buttons, NVDA will now say default.

## Version 23.02

* NVDA 2022.4 oder neuer wird benötigt.
* Windows 10 Version 21H2 (November 2021 Update bzw. Bbuild 19044) oder
  neuer wird benötigt.

## Version 23.01

* NVDA 2022.3 oder neuer ist erforderlich.
* Windows 10 oder neuer ist erforderlich, da Windows 8.1 ab Januar 2023
  nicht mehr von Microsoft unterstützt wird.
* Es ist möglich, die Befehle für die Touch-Tastatur und die
  Diktatumschaltung im Dialogfeld der Tastenbefehle unter der Kategorie
  "Erweiterte Touch-Gesten" neu zuzuweisen.
* Der Workaround für den schreibgeschützten Status von Touch-Tastatur-Tasten
  wurde entfernt, da er in Windows 10 behoben ist.

## Version 22.03

* NVDA 2021.3 oder neuer ist erforderlich.
* Beim Versuch, das Add-on unter Windows 7 und 8/8.1 zu installieren, wird
  eine Warnung angezeigt.

## Version 21.10

* NVDA 2021.2 oder neuer ist erforderlich, da die Änderungen diese
  Erweiterung betreffen.

## Version 21.08

* Unterstützung für Windows 11.

## Version 21.01

* NVDA 2020.3 oder neuer ist erforderlich.
* Unter Windows 10 Version 1709 und neuer wird die Diktierfunktion mit vier
  Fingern nach links wischen umgeschaltet (Windows+H).
* Dedizierter Umschaltbefehl für die Unterstützung zur Touch-Interaktion aus
  der Erweiterung entfernt.
* Da die Unterstützung der Touch-Interaktion über das Einstellungsfeld für
  die Berührungsinteraktion von NVDA umgeschaltet werden kann, wurde ein
  spezielles Einstellungsfeld für erweiterte Berührungsgesten entfernt.

## Version 20.09

* Möglichkeit entfernt, den NVDA die Berührungsinteraktion für bis zu zehn
  Sekunden abschalten zu lassen (Durchreichen der Touch-Befehle).
* Funktion für den Signalton für die Koordinatenrückmeldungen wurde
  entfernt.

## Version 20.07

* Es wurde ein Tastaturbefehl zum Umschalten der Touch-Interaktion oder zum
  Aktivieren bzw. Deaktivieren der Durchreichen des Touch-Befehls
  (Strg+Alt+NVDA+T) hinzugefügt.
* Da NVDA 2020.1 und neuer einen Touch-Befehl zur Ausführung eines rechten
  Mausklicks (ein Finger tippen und halten) enthält, wurde der Befehl aus
  dieser Erweiterung entfernt. Daher ist NVDA 2020.1 oder neuer
  erforderlich.
* Die Möglichkeit, NVDA die Touch-Interaktion für bis zu zehn Sekunden
  abschalten zu lassen (Durchreichen des Touch-Befehls), ist veraltet. In
  Zukunft wird diese Funktion stattdessen die Touch-Interaktion umschalten.
* In NVDA-Entwicklungs-Snapshots werden aufgrund von Änderungen der
  Touch-Interaktionsfunktion die Funktion zum Durchreichen von
  Touch-Befehlen und das Einstellungsfenster für erweiterte Berührungsgesten
  deaktiviert. Der zum Aktivieren des Durchreichens von touch-Befehlen
  verwendete Befehl schaltet stattdessen die Touch-Interaktion um.
* Die Funktion für den Signalton für die Koordinatenrückmeldungen ist
  veraltet und wird in einer zukünftigen Version entfernt werden.
* Der Signalton für die KoordinatenRückmeldung ertönt nicht, wenn die
  Tastatur mit Touch-Eingabe verwendet wird.
* NVDA wird nicht mehr den Anschein erwecken, nichts zu tun oder Fehlertöne
  abzuspielen, wenn moderne Eingabemöglichkeiten wie das Emoji-Panel per
  Berührung erkundet werden.
* NVDA gibt eine Fehlermeldung aus, wenn die Touch-Tastatur nicht aktiviert
  werden konnte (Mit vier Fingern nach rechts wischen).

## Version 20.06

* Mit Flake8 wurden viele Code-Probleme und potenzielle Fehler behoben.

## Version 20.04

* Rechte Mausklick-Geste (ein Fingertipp und Halten) ist jetzt Teil von NVDA
  2020.1.

## Version 20.01

* Benötigt NVDA 2019.3 oder neuer.
* Der Befehl zum Umschalten der Unterstützung für Touchscreens
  (einschließlich Durchreichen des Touch-Befehls) funktioniert nicht mehr,
  wenn dieser vollständig ausgeschaltet ist.

## Version 19.11

* Eingabehilfemeldungen für zusätzliche Berührungsgesten hinzugefügt.

## Version 19.09

* Die Touch-Unterstützung kann jetzt überall deaktiviert werden, nicht nur
  von anderen Profilen, sondern auch in der Standard-Konfiguration.

## Version 19.07

* Interne Änderungen zur Unterstützung zukünftiger NVDA-Versionen.

## Version 18.12

* Interne Änderungen zur Unterstützung zukünftiger NVDA-Versionen.

## Version 18.08

* Kompatibel mit NVDA 2018.3 und zukünftigen Versionen.

## Version 18.06

* Einstellungen für die Erweiterung finden Sie nun im neuen
  NVDA-Einstellungsbildschirm unter der Kategorie "Erweiterte
  Touch-Gesten". Daher ist NVDA 2018.2 erforderlich.
* Kompatibilitätsprobleme mit wxPython 4 behoben.

## Version 18.04

* Behebt ein Problem, bei dem die Touch-Interaktionskategorie im
  NVDA-Einstellungsfenster aufgrund von vorgenommenen Änderungen durch die
  Erweiterung zu Fehlertönen führen kann.

## Version 18.03

* NVDA 2018.1 ist erforderlich.
* Das Kontrollkästchen "Tippen auf Berührung" ist nun im NVDA selbst
  integriert, deshalb wurde dieses Kontrollkästchen aus der Erweiterung
  ausgegliedert.

## Version 17.12

* Erfordert NVDA 2017.4. Diese Erweiterung unterstützt nun auch das Wechseln
  der Konfigurationsprofile im NVDA.
* Da NVDA 2017.4 die Ansage der Bildschirmausrichtung  enthält, ist diese
  Funktion nicht mehr Bestandteil der Erweiterung.
* Ein verstecktes Kontrollkästchen im Dialogfeld"Touch-Interaktion" wurde
  hinzugefügt, um die Touch-Unterstützung vollständig zu deaktivieren. Dies
  ist nur für benutzerdefinierte Konfigurationsprofile verfügbar.
* Wenn NVDA 2018.1 oder neuer verwendet wird, wird der Dialog Interaktion
  berühren zweimal im Einstellungsmenü von NVDA aufgeführt. Das zweite
  Element ist der Dialog, der mit der Erweiterung mitgeliefert wird.
* Im Erweiterungsdialog Touch Interaction nwird die Eingabeart "Tippen auf
  Berührung" nicht mehr angezeigt, wenn NVDA 2018.1 verwendet wird.

## Version 17.10

* Aufgrund der Support-Richtlinien von Microsoft wird Windows 8
  (Originalversion) nicht mehr unterstützt. Windows 8.1 ist daher
  erforderlich.
* NVDA wird die Bildschirmausrichtung nicht mehr zweimal ankündigen, wenn
  NVDA 2017.4 Entwicklungs-Snapshots ausgeführt werden.

## Version 17.07.1

* Eine Option im Dialogfeld für die Touch-Interaction wurde hinzugefügt, um
  das Durchreichen von  Touch-Gesten ohne Verwendung eines Timers manuell
  umzuschalten.
* Bei ausgeschaltetem manuellen Durchreichmodus würde die Touch-Interaction
  aktiviert werden, wenn das manuelle Durchreichen der Befehle vor dem
  ablaufen der Durchreichezeit eingeschaltet wird.

## Version 17.07

* Ein neues Dialog namens Touch-Interaction wurde unter NVDA-Menü /
  Einstellungen hinzugefügt, um das Verhalten von NVDA während der Nutzung
  von Touchscreens zu konfigurieren.
* Nach der Installation dieser Version muss man beim Drücken von Tasten auf
  der Touch-Tastatur die gewünschte Taste doppelt antippen. Sie können auf
  die alte Art der Eingabe zurückschalten, indem Sie die Eingabeart Tippen
  auf Berührung im Dialogfeld"Touch-Interaction" aktivieren.
* Ein neuer, noch nicht zugewiesener Befehl wurde hinzugefügt, welcher die
  Berührungsgeste bis zu 10 Sekunden an das Gerät / die Anwendung
  durchreicht.
* Es wurde eine neue Option im Dialogfeld Touch-Interaction hinzugefügt. Sie
  erlaubt NVDA die Touch-Interaction zwischen 3 und 10 Sekunden
  durchzureichen, um Touchscreen-Gesten direkt auszuführen (als ob NVDA
  beendet wäre). Der Standardwert liegt bei 5 Sekunden.
* Debug-Logging-Meldungen werden nun beim Ausführen von Rechtsklicks (Tippen
  und Halten) im NVDA-Protokoll aufgezeichnet. Erfordert NVDA 2017.1 oder
  höher.
* Aufgrund von Änderungen bei der Wiedergabe von Bildschirmkoordinaten ist
  NVDA 2017.1 oder höher erforderlich.

##Version 17.03

* Ein problem wurde behoben, wo bei der Verwendung von NVDA 2017.1 oder
  höher der Piepton der Koordinatenansage nicht abgespielt oder ein Fehler
  wiedergegeben wurde.

##Version 16.12

* Web-Touch-Modus funktioniert in allen Anwendungen, wo der Lesemodus
  (browse mode) unterstützt wird. Dies sind beispielsweise Microsoft Edge,
  Microsoft Word, Kindle, Firefox usw.
* Listen und Sprungmarken sind nun Teile der Web-Touch-Elemente.

## Version 16.06

* Ehrstveröffentlichung der stabilen Version.

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
