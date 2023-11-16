# instantTranslate #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

Deze add-on kan geselecteerde tekst of tekst van het klembord vertalen. Dit
wordt gedaan met de Google Translate dienst.

## Talen instellen ##
To configure source, target and in case swap language, from NVDA menu, go to
Preferences, then go to Instant Translate Settings.  There are three combo
boxes labeled "translate from", "translate into" and "Language for swapping"
(if you selected auto option from source languages).

If you selected the auto option from source languages, there is also a
checkbox about the auto-swap: if you activate it, then the addon tries to
commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combo is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

However, this is a temporary configuration, if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below.

## Hoe gebruikt u deze add-on ##
Er zijn twee manieren om deze add-on te gebruiken:

1. Select some text using selection commands (shift with arrow keys, for
   example). Then press Shift+NVDA+T to translate the selected text. Then
   the translated string will be read, providing that the synthesizer you
   are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NVDA+Y to translate the
   text in the clipboard to the target language.

## Other useful commands ##
* NVDA+shift+r: pressed once, announce current configuration; pressed twice,
  swap source and target languages.

## Changes for 3.0 ##
* Implemented swapping languages.
* Changed configuration format, now we can change instant translate settings
  if we are in readonly pane, but remember that this will work before first
  restart of nvda.
* Removed limit on amount of text that can be translated.
* Sneltoets t toegevoegd aan het menu-item Instellingen voor Instant
  Translate
* The auto option is now in first position in source combo, and absent in
  target combo.
* Selectievakje toegevoegd voor het configureren van het kopiëren van
  vertaalresultaten.
* Het configuratiebestand wordt opgeslagen in de root van de
  instellingenmap.
* Nieuwe vertalingen: Aragonees, Arabisch, Braziliaans Portuguees,
  Kroatisch, Nederlands, Fins, Frans, Gallisch, Duits, Hongaars, Italiaans,
  Japans, Koreaans, Nepali, Pools, Slovaaks, Sloveens, Spaans, Tamil, Turks.

## Veranderingen voor 2.1 ##
* De add-on kan nu tekst vertalen van het klembord als u nvda+shift+y drukt.

## Veranderingen voor 2.0 ##
* Gui configurator toegevoegd waar u de bron- en doeltaal kunt kiezen.
* U vindt de add-on nu in het menu onder Instellingen.
* De instellingen worden nu opgeslagen in een apart configuratiebestand.
* De vertaalresultaten komen automatisch op het klembord zodat u er verder
  mee kunt werken.

## Veranderingen voor 1.0 ##
* Eerste versie.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
