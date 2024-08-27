# Udvidede berøringsfunktioner) #

* Forfatter: Joseph Lee
* Download [stabil version][1]
* NVDA compatibility: 2022.4 and later

Dette tilføjelsesprogram tilføjer ekstra berøringskommandoer til NVDA. Det
giver et sæt bevægelser for lettere navigering i gennemsynstilstand.

Note: this add-on requires NVDA 2022.3 or later running on a touchscreen
computer with Windows 10 or 11.

## Kommandoer

### Tilgængelig over alt

* Dobbelt-tap med 4 fingre: Slå hjælpetilstand til/fra.
* Svirp til højre med 4 fingre: Slå berøringstastatur til/fra (som regel
  til).
* Svirp med fire fingre til venstre: Aktivér eller deaktivér diktering
  (Windows+H; Windows 10 version 1709 eller nyere).

### Objekttilstand

* Svirp ned med tre fingre: Læs aktuelle vindue.
* Svirp til venstre med 3 fingre: Annoncer objekt med fokus.
* Svirp til højre med 3 fingre: Annoncer aktuelle navigator-objekt.
* Svirp op med 4 fingre: Annoncer titel på aktuelle vindue.
* Svirp ned med 4 fingre: Annoncer tekst på statuslinjen.

## Web-berøringstilstand

Med denne berøringstilstand, som kan bruges i gennemsynstilstand, kan du
navigere i et dokument efter det valgte element. I dokumenter, der
understøtter gennemsynstilstand, kan du skifte til web-tilstand ved at tappe
med 3 fingre. I denne tilstand kan du svirpe op og ned med en finger for at
vælge den type element, du vil navigere efter. Du kan svirpe mod højre eller
venstre flytter til henholdsvis det næste eller forrige element af den
valgte type. Når du går ud af et dokument, som understøtter
gennemsynstilstand, vil objektberøringstilstand blive brugt.

## Berøringstilstand til indstilling af talesyntese

Du kan bruge denne tilstand til hurtigt at at skifte indstillinger for
talesyntese, f.eks. vælge en stemme og ændre lydstyrke. I denne tilstand kan
du svirpe til højre eller venstre med to fingre for at flytte mellem de
forskellige indstillinger for talesyntesen. Svirp op og ned for at ændre den
valgte indstilling. Disse bevægelser svarer til tastaturkommandoerne til
ringen for talesynteseindstillinger.

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

* NVDA 2021.3 eller nyere er påkrævet.
* En advarselsmeddelelse vil blive vist, når du forsøger at installere
  tilføjelsen på Windows 7, 8 og 8.1.

## Version 21.10

* NVDA 2021.2 eller nyere er påkrævet på grund af ændringer til NVDA, der
  påvirker denne tilføjelse.

## Version 21.08

* Første understøttelse til Windows 11.

## Version 21.01

* NVDA 2020.3 eller nyere er påkrævet.
* I Windows 10 Version 1709 og senere vil et svirp med fire fingre til
  venstre slå diktering til eller fra(Windows+H).
* Fjernet berøringsinteraktionskommando fra tilføjelsen.
* Da understøttelse af berøringsinteraktion kan skiftes fra NVDA's panel for
  berøringsinteraktionsindstillinger, er et særligt panel med forbedrede
  berøringsbevægelser blevet fjernet.

## Version 20.09

* Fjernet indstillingen til at lade NVDA deaktivere berøringsinteraktion i
  op til ti sekunder (slip bevægelser direkte igennem til systemet).
* Fjernede funktionen for annoncering af koordinater som lydsignal

## Version 20.07

* Tilføjede en tastaturkommando til at skifte berøringsinteraktion eller
  aktivere/deaktivere  funktion, der slipper berøringsbevægelser igennem, så
  bevægelser ikke indfanges af NVDA (Ctrl+Alt+NVDA+T).
* Da NVDA 2020.1 og nyere inkluderer en touch-kommando til at udføre
  højreklik med musen (tryk og hold på en finger), er kommandoen blevet
  fjernet fra denne tilføjelse. Derfor kræves NVDA 2020.1 eller nyere.
* Muligheden for at lade NVDA slå berøringsinteraktion fra i op til ti
  sekunder (funktion til at slippe bevægelser direkte igennem til systemet)
  er forældet. I fremtiden skifter denne kommando i stedet for indstillingen
  for berøringsinteraktion.
* I NVDA-udviklingssnapshots, på grund af ændringer i
  berøringsinteraktionsfunktionen, vil berøringskommandoens funktion til at
  slippe bevægelser direkte igennem til operativsystemet blive
  deaktiveret. Den kommando, der bruges til at aktivere denne funktion, vil
  nu slå berøringsinteraktion til og fra i stedet.
* Koordinat-meddelelsesbip-funktionen er forældet og fjernes i en fremtidig
  tilføjelsesopdatering.
* Koordinat-meddelelsesbip høres ikke, mens du bruger berøringstastaturet.
* NVDA vil ikke længere se ud til at gøre ingenting eller afspille
  fejletoner, mens man udforsker moderne inputmetoder såsom emoji-panelet
  via berøring.
* NVDA vil vise en fejlmeddelelse, hvis berøringstastaturet ikke kan
  aktiveres (svirp fire fingre til højre).

## Version 20.06

* Løst mange problemer med kodningstil og potentielle fejl med Flake8.

## Version 20.04

* Højre museklik (tryk og hold med én finger) er nu en del af NVDA 2020.1.

## Version 20.01

* NVDA 2019.3 eller nyere er påkrævet.
* Kommandoen til at slå understøttelse for berøring til og fra (herunder
  muligheden for at slippe bevægelser direkte igennem) fungerer ikke
  længere, hvis berøringsunderstøttelse er slået helt fra.

## Version 19.09

* Tilføjede meddelelser for inputhjælp til yderligere berøringskommandoer.

## Version 19.09

* Berøringsunderstøttelse kan nu deaktiveres fra alle steder, ikke kun fra
  andre profiler end den normale profil.

## Version 19.07

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Version 18.12

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Version 18.08

* Kompatibel med NVDA 2018.3 og fremtidige versioner.

## Version 18.06

* Tilføjelsesindstillinger er nu at finde i kategorien "Udvidede
  berøringsbevægelser" i NVDAs indstillingsdialog. Som følge heraf er NVDA
  2018.2 påkrævet.
* Rettede kompatibilitetsproblemer med wxPython 4.

## Version 18.04

* Løser et problem, hvor indstillingskategorien "Berøringsinteraktion"i
  NVDA-indstillingspanelet kan forårsage fejllyde, der høres på grund af
  ændringer foretaget af denne tilføjelse.

## Version 18.03

* NVDA 2018.1 er påkrævet.
* Fordi NVDA 2018.1 kommer med check box til at slå berøringsindtastning til
  og fra, er afkrydsningsfeltet ikke længere inkluderet i denne tilføjelse.

## Version 17.12

* Kræver NVDA 2017.4. Specifikt, kan denne tilføjelse nu håndtere skift af
  indstillingsprofiler.
* Da NVDA 2017.4 omfatter meddelelser om skærmens orientering, er denne
  funktion ikke længere en del af denne tilføjelse.
* Tilføjede en skjult check box i berøringsinteraktion, der lader dig slå
  understøttelse for berøring helt fra (tilgængelig hvis andre profiler end
  den normale indstillingsprofil er aktiv).
* Hvis du bruger NVDA 2018.1 eller nyere, vil du få vist dialoger til
  berøringsinteraktion to gange under NVDAs indstillingskategorier. Det
  andet punkt er den dialog, der tilhører tilføjelsen.
* Indstillingen til berøringsindtastning vises ikke længere i tilføjelsens
  egen dialog for berøringsindtastning, hvis du benytter NVDA 2018.2 eller
  nyere.

## Version 17.10

* På grund af støttepolitik fra Microsoft understøttes Windows 8 (original
  version) ikke længere.
* NVDA meddeler ikke længere skærmorientation to gange, når du kører NVDA
  2017.4 development snapshots.

## Version 17.07.1

* Tilføjet en mulighed i dialogboksen "Berøringsinteraktion" til at manuelt
  lade berøringsbevægelser slippe igennem, uden at bruge en timer.
* Med tilstanden til manuelt at slippe berøringsbevægelser igennem slået
  fra, og hvis berøringsbevægelser slippes igennem før varigheden udløber,
  slås berøringsinteraktion til.

## Version 17.07Version: [0.6][1]

* Tilføjet en ny dialogboks ved navn "Berøringsindtastning" under NVDAs menu
  under Præferencer til at konfigurere, hvordan NVDA fungere med
  berøringsskærme.
* Du skal trykke to gange på den ønskede tast på berøringstastaturet, når du
  har installeret denne version. Du kan skifte tilbage til den forrige
  metode ved at benytte dialogen "Beræringsindteraktion".
* Tilføjede en utildelt kommando, der lader NVDA ignorere alle
  berøringsbevægelser op til 10 sekunder.
* Tilføjet en mulighed i dialogen "Berøringsinteraktion", der tillader NVDA
  at pause berøringsinteraktion mellem 3 til 10 sekunder for at udføre
  bevægelser direkte (som om NVDA ikke kørte, standard er 5 sekunder).
* Tilføjede beskeder ang. fejlfinding når du udføre højreklik (tryk og hold
  nede), der skrives ind i din NVDA-logfil. Dette kræver NVDA 2017.1 eller
  nyere.
* På grund af ændringer, der foretages ved afspilning af skærmkoordinater,
  kræves NVDA 2017.1 eller nyere.

##Version 17.03

* Løst et problem, hvor bip når koordinater blev annoncerede ikke spillede
  eller en fejltone blev spillet i stedet, når du bruger NVDA 2017.1 eller
  nyere.

##Version 16.12

* Web-berøringstilstand fungerer i Microsoft Edge, Microsoft Word og andre
  hvor steder gennemsynstilstand benyttes.
* Tilføjede lister og landmærker til elementer af web-berøringstilstande.

## Version 16.06

* Første stabile version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
