# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Descărcați [versiunea stabilă][1]
* NVDA compatibility: 2022.4 and later

Acest supliment oferă gesturi adiționale de atingere a ecranului pentru
NVDA. El de asemenea oferă un set de gesturi pentru o navigare mai ușoară.

Note: this add-on requires NVDA 2022.3 or later running on a touchscreen
computer with Windows 10 or 11.

## Comenzi

### Disponibile oriunde

* Atingere dublă cu 4 degete: comută modul de intrare al ajutorului.
* Glisare la dreapta cu 4 degete: comută tastatura tactilă (de obicei o
  activează).
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version
  1709 or later).

### Mod obiect

* Glisare în jos cu 3 degete: citește fereastra curentă.
* Glisare la stânga cu 3 degete: anunță obiectul curent cu focalizarea.
* Glisare la dreapta cu 3 degete: anunță obiectul navigator curent.
* Glisare în sus cu 4 degete: anunță titlul ferestrei curente.
* Glisare în jos cu 4 degete: anunță textul barei de stare.

## Mod tactil web

Acest mod tactil, disponibil în modul navigare, vă permite să parcurgeți
documentul prin elementul selectat. Pentru a comuta la modul web din
documentele modului de navigare, efectuați o atingere cu 3 degete. Din acest
mod, glisând în sus sau în jos cu un deget prin intermediul modurilor de
navigare a elementelor disponibile, în timp ce faceți clic dreapta sau
stânga cu un deget se deplasează la elementul următor sau anterior ales.După
ce vă îndepărtați de documentele de navigare, este utilizat modul de
atingere a obiectului.

## Setările sintetizatorului la modul de atingere

Aveți posibilitatea să utilizați acest mod pentru a modifica rapid setările
de sintetizator, cum ar fi alegerea unei voci și modificarea volumului. În
acest mod, utilizați glisarea cu două degete spre stânga sau spre dreapta
pentru a vă deplasa între setările sintetizatorului și utilizați gesturile
glisare cu două degete sus și jos pentru a modifica valorile. Aceste gesturi
reflectă asta în comenzile setărilor sintezei pe tastatură.

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

## Version 20.09

* Removed ability to let NVDA turn off touch interaction for up to ten
  seconds (touch command passthrough).
* Removed coordinate announcement beep feature.

## Version 20.07

* Added a keyboard command to toggle touch interaction or enable/disable
  touch passthrough (Control+Alt+NVDA+T).
* As NVDA 2020.1 and later includes a touch command to perform right mouse
  click (one finger tap and hold), the command has been removed from this
  add-on. AS a result, NVDA 2020.1 or later is required.
* The ability to let NVDA turn off touch interaction for up to ten seconds
  (touch command passthrough) is deprecated. In the future this feature will
  toggle touch interaction instead.
* In NVDA development snapshots, due to touch interaction feature changes,
  touch command passthrough feature and Enhanced Touch Gestures settings
  panel will be disabled. The command used to enable touch command
  passthrough will toggle touch interaction instead.
* Coordinate announcement beep feature is deprecated and will be removed in
  a future add-on release.
* Coordinate announcement beep will not be heard while using touch keyboard.
* NVDA will no longer appear to do nothing or play error tones while
  exploring modern input facility such as emoji panel via touch.
* NVDA will present an error message if touch keyboard cannot be activated
  (four finger flick right).

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Right mouse click gesture (one finger tap and hold) is now part of NVDA
  2020.1.

## Versiunea 20.01

* Este necesar NVDA 2019.3 sau mai nou.
* Comenzile de activare ale suportului tactil (inclusiv atingerea
  passthrough) nu vor mai funcționa dacă suportul tactil este complet
  inactiv.

## Versiunea 19.11

* Au fost adăugate mesaje explicative pentru comenzile tactile suplimentare.

## Versiunea 19.09

* Suportul tactil poate fi dezactivat de oriunde, nu doar din alte profiluri
  decât cel normal.

## Versiunea 19.07

* Modificări interne care suportă viitoarele versiuni de NVDA.

## Versiunea 18.12

* Modificări interne care suportă viitoarele versiuni de NVDA.

## Versiunea 18.08

* Compatibil cu NVDA 2018.3 și cu versiuni viitoare.

## Versiunea 18.06

* Setările suplimentului se află în ecranul multicategoriei de setări, în
  categoria „Enhanced Touch Gestures”. Ca rezultat al acestei schimbări,
  este necesară versiunea NVDA 2018.2.
* S-au rezolvat problemele de compatibilitate cu wxPython 4.

## Versiunea 18.04

* Rezolvă o problemă în care categoria interacțiunii tactile din panoul de
  setări al NVDA-ului poate cauza auzirea sunetelor de eroare datorită
  modificărilor făcute n acest supliment.

## Versiunea 18.03

* Este necesar NVDA 2018.1.
* Fiindcă NVDA 2018.1 vine la pachet cu caseta de bifat „„scriere tactilă”,
  ea nu mai este inclusă în acest supliment.

## Versiunea 17.12

* Necesită NVDA 2017.4. De specificat: acest supliment poate gestiona acum
  comutările configurații profilurilor.
* Întrucât NVDA 2017.4 include anunțarea orientării ecranului, această
  caracteristică nu mai face parte din supliment.
* S-a adăugat o casetă de bifat ascunsă în dialogul interacțiunii tactile
  pentru dezactivarea completă a suportului tactil (disponibilă dacă sunt
  active alte profiluri decât configurația obișnuită).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* În dialogul interacțiunii tactile pentru supliment, modul de scriere
  tactilă nu mai este afișat dacă se utilizează NVDA 2018.1 sau mai nou.

## Versiunea 17.10

* Datorită politicii de asistență de la Microsoft, Windows 8 (versiunea
  originală) nu mai este suportată.
* NVDA nu va mai anunța orientarea ecranului de două ori atunci când se
  rulează versiuni de dezvoltare snapshot NVDA 2017.4.

## Versiunea 17.07.1

* A fost adăugată o opțiune în dialogul de interacțiune prin atingere pentru
  comutarea manuală între activarea și dezactivarea trecerii prin atingere
  fără utilizarea unui cronometru.
* Cu opțiunea de trecere manuală dezactivată, dacă trecerea prin atingere
  este activat înainte de expirarea duratei de trecere, atingerea
  interacțiunii va fi activată.

## Versiunea 17.07

* A fost adăugat un nou dialog numit Interacțiunea prin atingere în meniul
  de preferințe al NVDA-ului pentru a configura cum să lucreze NVDA-ul cu
  ecranele tactile.
* După instalarea acestei versiuni, atunci când apăsați tastele de pe
  tastatura tactilă, trebuie să atingeți dublu tasta dorită. Puteți reveni
  la modul vechi, permițând introducerea de atingeri din dialogul
  Interacțiune prin atingere.
* A fost adăugată o comandă (neatribuită) pentru a-i permite NVDA-ului să
  ignore gesturile de atingere timp de 10 secunde.
* A fost adăugată o opțiune în dialogul Interacțiunea prin atingere pentru a
  permite NVDA să întrerupă interacțiunea tactilă între 3 și 10 secunde
  pentru a efectua direct gesturile de pe ecranul tactil (ca și când NVDA nu
  se execută, implicit este de 5 secunde).
* Au fost adăugate mesajele de diagnosticare la efectuarea click-urilor
  dreapta (atingeți și țineți apăsat) pentru a fi înregistrate în jurnalul
  NVDA (necesită NVDA 2017.1 sau mai nou).
* Datorită schimbărilor făcute la redarea coordonatelor ecranului, NVDA
  2017.1 este necesar.

##Version 17.03

* A fost reparată o eroare în care bipul anunțării coordonatelor nu era
  redat, iar în locul lui o eroare de ton era redată la utilizarea NVDA
  2017.1 sau mai nou.

##Version 16.12

* Modul tactil web funcționează în Microsoft Edge, Microsoft Word, și altele
  unde unde modul navigare este folosit.
* Au fost adăugate liste și puncte de reper pentru elementele modului tactil
  web.

## Versiunea 16.06

* Versiunea stabilă inițială.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
