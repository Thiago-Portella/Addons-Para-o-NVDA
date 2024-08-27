# Pokročilé dotykové gestá #

* Autor: Joseph Lee
* Stiahnuť [stabilnú verziu][1]
* NVDA compatibility: 2022.4 and later

Poskytuje doplnkové dotykové gestá na ovládanie NVDA a tiež gestá pre prácu
v režime prehliadania.

Note: this add-on requires NVDA 2022.3 or later running on a touchscreen
computer with Windows 10 or 11.

## Príkazy

### Všeobecné

* Poklepanie štyrmi prstami: Aktivuje a deaktivuje nápovedu vstupu.
* Švihnutie vpravo štyrmi prstami: Aktivuje dotykovú klávesnicu.
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version
  1709 or later).

### Objektový režim

* Švihnutie dole troma prstami: Prečíta názov aktuálneho okna.
* Švihnutie vľavo troma prstami: Oznámi zameraný objekt.
* Švihnutie vpravo troma prstami: Oznámi navigačný objekt.
* Švihnutie hore štyrmi prstami: Oznámi názov aktuálneho okna.
* Švihnutie dole štyrmi prstami: Oznámi stavový riadok.

## Webový režim

Tento režim umožňuje prezeranie dokumentov a prechádzanie po jednotlivých
prvkoch dokumentu. Webový režim aktivujete v režime prehliadania poklepaním
troma prstami. Švihaním hore a dole následne prechádzate medzi dostupnými
prvkami. Švihaním doľava a doprava potom skáčete po vybratých prvkoch. Po
opustení dokumentu sa automaticky aktivuje objektový režim.

## Nastavenia kruhu hlasového výstupu

Pomocou dotykových gest môžete rovnako ako z klávesnice okamžite upravovať
nastavenia hlasového výstupu. Švihaním dvoma prstami vľavo a vpravo
vyberiete parameter, ktorý chcete zmeniť. Švihaním dvoma prstami hore a dole
následne upravujete hodnoty.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 8.1 is no longer supported by
  Microsoft as of January 2023.
* It is possible to reassign touch keyboard and dictation toggle commands
  from input gestures dialog under Enhanced Touch Gestures category.
* Removed read-only state workaround for touch keyboard keys as it is
  resolved in Windows 10.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Initial support for Windows 11.

## Version 21.01

* NVDA 2020.3 or later is required.
* On Windows 10 Version 1709 and later, doing a four finger flick left will
  toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction
  settings panel, a dedicated Enhanced Touch Gestures settings panel has
  been removed.

## Verzia 20.09

* Odstránená funkcia na dočasné vypnutie dotykových gest.
* Odstránené signalizovanie polohy.

## Verzia 20.07

* Pridaná skratka na zapínanie a vypínanie ovládania pomocou dotykovej
  obrazovky.
* NVDA od verzie 2020.1 obsahuje dotykové gesto simulujúce kliknutie pravým
  tlačidlom myši. Preto bola táto funkcia z doplnku odstránená. Zároveň to
  znamená, že doplnok správne funguje v NVDA od verzie 2020.1.
* Funkcia dočasného vypnutia ovládania pomocou dotykov sa viac nevyvíja a
  máme v pláne ju odstrániť. Skratka bude v budúcnosti len zapínať a vypínať
  ovládanie pomocou dotykovej obrazovky.
* Vzhľadom na zmeny v dotykových gestách vo vývojových verziách NVDA je v
  týchto verziách nedostupný panel nastavení doplnku. Klávesová skratka
  vypína alebo zapína ovládanie pomocou dotykovej obrazovky.
* Oznamovanie pozície zvukom sa viac nevyvíja a bude čoskoro odstránené.
* NVDA pri používaní dotykovej klávesnice neoznamuje pozíciu zvukom.
* NVDA viac nezamrzne pri prezeraní emoji panela a podobných prvkov pomocou
  dotykových gest.
* NVDA zobrazí chybu, ak nie je možné zobraziť dotykovú klávesnicu.

## Verzia 20.06

* Oopravené drobné chyby v kóde.

## Verzia 20.04

* Gesto na simulovanie kliknutia pravým tlačidlom myši je priamo súčasťou
  NVDA 2020.1.

## Verzia 20.01

* Vyžaduje NVDA od verzie 2019.3.
* Ak je vypnutá podpora pre dotykové gestá, vypnú sa aj gestá na zapínanie a
  vypínanie pokročilých gest a tiež gesto na prepustenie dotykov.

## Verzia 19.11

* Pridané texty do nápovedy vstupu.

## Verzia 19.09

* Gestá sa dajú vypnúť kedykoľvek, aj v iných profiloch.

## Verzia 19.07

* Interné zmeny, príprava na podporu budúcich verzií NVDA.

## Verzia 18.12

* Interné zmeny, príprava na podporu budúcich verzií NVDA.

## Verzia 18.08

* Vyžaduje NVDA od verzie 2018.3.

## Verzia 18.06

* Nastavenia presunuté do stromu nastavení NVDA.
* Opravená kompatibilita s wxPython 4.

## Verzia 18.04

* Pri zmene nastavení viac NVDA neprehráva chybový zvuk.

## Verzia 18.03

* Vyžaduje NVDA 2018.1.
* Odstránené nastavenie Písať okamžite po dotyku, keďže táto funkcia je
  súčasťou NVDA.

## Verzia 17.12

* Vyžaduje NVDA 2017.4. Umožňuje mať špecifické nastavenia v konfiguračných
  profiloch.
* Keďže táto verzia NVDA oznamuje orientáciu obrazovky, bola táto funkcia
  odstránená z doplnku.
* Pridané začiarkávacie políčko na vypnutie podpory dotyku (ak je aktívny
  iný ako normálny profil).
* V NVDA od verzie 2018.1 je v menu dialóg s nastaveniami pre dotykové gestá
  dvakrát. Druhý patrí k tomuto doplnku.
* Funkcia písať okamžite po dotyku nie je dostupná, ak používate NVDA od
  verzie 2018.1.

## Verzia 17.10

* Odstránená podpora pre Windows 8.
* NVDA vo vývojovej verzii 2017.4 neoznamuje dvakrát orientáciu obrazovky.

## Verzia 17.07.1

* Pridaná možnosť ručne prepínať prepustenie dotykov bez časovača.
* Ak aktivujete prepustenie pred uplynutím času predchádzajúceho
  prepustenia, prepustenie sa deaktivuje a aktivuje sa normálne správanie
  NVDA.

## Verzia 17.07

* Pridané nastavenia doplnku.
* Po nainštalovaní doplnku funguje písanie tak, že je potrebné na príslušný
  znak poklepať. Môžete začiarknúť funkciu písať okamžite po dotyku v
  nastaveniach doplnku.
* Pridaná možnosť ignorovať dotykové gestá (prepustenie do 10 sekúnd).
* Pridaná možnosť nastaviť dĺžku prepustenia. V tomto čase sa budú gestá
  posielať priamo do systému, ako keby nebolo NVDA spustené.
* Do záznamu sa pridávajú informácie pri gesteklepnúť a podržať (vykonáva
  kliknutie pravým tlačidlom myši). Toto správne funguje len v NVDA od
  verzie 2017.1.
* Vyžaduje sa NVDA od verzie 2017.1, hlavne pre zmeny, ktoré sa urobili v
  NVDA na oznamovanie pozície myši zvukom.

##Version 17.03

* Opravené oznamovanie pozície kurzora myši zvukom pre NVDA od verzie
  2017.1.

##Version 16.12

* Webový režim funguje v aplikáciách MS Edge, Word a ďalších.
* Do webového režimu pridaná možnosť prechádzať po oblastiach stránky a
  zoznamoch.

## Verzia 16.06

* Prvé stabilné vydanie.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
