# Dodatne dodirne geste (Enhanced touch gestures) #

* Autor: Joseph Lee
* Preuzmi [stabilnu verziju][1]
* NVDA kompatibilnost: 2022.4 i novije verzije

Ovaj dodatak omogućuje dodatne dodirne geste na ekranu za dodir u NVDA
čitaču. Ovaj dodatak također dodaje skup dodirnih gesti za lakše kretanje u
modusu čitanja.

Napomena: Ovaj dodatak zahtijeva NVDA 2022.3 ili noviju verziju koja se
koristi na računalu s ekranom koji je osjetljiv na dodir, s instaliranim
sustavom Windows 10 ili 11.

## Naredbe

### Svuda dostupne

* Dodir s četiri prsta: uključi ili isključi modus pomoći tijekom unosa.
* Klizanje s četiri prsta u desno: uključi ili isključi dodirnu tipkovnicu
  (obično je uključuje).
* Klizanje s četiri prsta u desno: uključi ili isključi diktiranje
  (Windows+H; Windows 10 verzija 1709 ili novija).

### Objektni modus

* Klizanje s tri prsta prema dolje: čita trenutačni prozor.
* Klizanje s tri prsta u lijevo: izvještava o objektu koji ima fokus.
* Klizanje s tri prsta u desno: izvještava o trenutačnom navigacijskom
  objektu.
* Klizanje s četiri prsta prema gore: izgovara naslov trenutačnog prozora.
* Klizanje s četiri prsta prema dolje: čita tekst statusne trake.

## Dodirni modus za web

Ovaj dodirni modus – dostupan u modusu čitanja – omogućuje kretanje po
označenom elementu. Za prebacivanje iz dokumenata u modusu čitanja u dodirni
modus za web, ekran treba dodirnuti s tri prsta. U ovom modusu, klizanjem
jednim prstom prema gore ili dolje prebacuje se između dostupnih modusa
kretanja po elementima. Klizanjem jednim prstom u desno ili u lijevo, pomiče
se na sljedeći ili prethodni element. Kad se izađe iz dokumenata u modusu
čitanja, koristi se dodirni modus za objekte.

## Postavke govorne jedinice u dodirnom modusu

Ovaj se modus koristiti za brzo mijenjenje postavki govorne jedinice, poput
odabira glasa ili promjene glasnoće. Klizanjem s dva prsta u lijevo ili
desno prelazi se između postavki govorne jedinice. Klizanjem s dva prsta
prema gore i dolje mijenjaju se vrijednosti. Ove su geste preslika prečaca s
tipkovnice.

## Verzija 23.02

* Potrebna je NVDA verzija 2022.4 ili novija.
* Potreban je sustav Windows 10 21H2 (aktualizirana verzija iz studenog
  2021./izgradnja 19044) ili novija verzija.

## Verzija 23.01

* Zahtijeva NVDA 2022.3 ili noviju verziju.
* Zahtijeva Windows 10 ili noviju verziju, jer od siječnja 2023. Microsoft
  više ne pordržava Windows 8.1.
* Moguće je ponovo dodijeliti dodirnu tipkovnicu i naredbe za prebacivanje
  diktata u dijaloškom okviru za ulazne geste u kategoriji „Dodatne dodirne
  geste”.
* Uklonjeno je zaobilazno rješenje stanja samo-za-čitanje za tipke dodirne
  tipkovnice budući da je to riješeno u sustavu Windows 10.

## Verzija 22.03

* Zahtijeva NVDA 2021.3 ili noviju verziju.
* Prikazat će se poruka upozorenja kad pokušaš instalirati dodatak na
  Windows 7, 8 i 8.1.

## Verzija 21.10

* Zahtijeva NVDA 2021.2 ili noviju verziju zbog promjena u NVDA čitaču koje
  utječu na ovaj dodatak.

## Verzija 21.08

* Izvorna podrška za Windows 11.

## Verzija 21.01

* Zahtijeva NVDA 2020.3 ili noviju verziju.
* On Windows 10 Version 1709 and later, doing a four finger flick left will
  toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction
  settings panel, a dedicated Enhanced Touch Gestures settings panel has
  been removed.

## Verzija 20.09

* Uklonjena je mogućnost, da NVDA isključi dodirnu interakciju do deset
  sekundi (prolaz naredbe dodirom).
* Ukljonjena je funkcija izvještavanja koordinata zvukom.

## Verzija 20.07

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

## Verzija 20.06

* Riješen je mnogo problema sa stilom kodiranja i potencijalnih grešaka s
  Flake8.

## Verzija 20.04

* Gesta za pritiskanje desnog gumba miša (dodir i držanje s jednim prstom)
  sada je dio NVDA čitača 2020.1.

## Verzija 20.01

* Zahtijeva NVDA 2019.3 ili noviju.
* Naredba za prebacivanje podrške dodira (uključujući proslijeđivanje) više
  neće funkcionirati, ako je podrška dodira potpuno isključena.

## Verzija 19.11

* Dodane su poruke pomoći tijekom unosa za dodatne dodirne naredbe.

## Verzija 19.09

* Podrška za dodir se sad može svugdje isključiti, ne samo u profilima koji
  nisu normalni profili.

## Verzija 19.07

* Unutarnje promjene, kako bi se podržale buduća NVDA izdanja.

## Verzija 18.12

* Unutarnje promjene, kako bi se podržale buduća NVDA izdanja.

## Verzija 18.08

* Kompatibilno s NVDA 2018.3 i budućim verzijama.

## Verzija 18.06

* Postavke dodatka se sada nalaze u novom ekranu NVDA postavki s višestrukim
  kategorijama pod kategorijom „Dodatne dodirne geste”. Iz tog razloga je
  potreban NVDA 2018.2.
* Ispravljena greška kompatibilnosti s wxPython 4.

## Verzija 18.04

* Ispravljena greška gdje kategorija Interakcija dodirom u postavkama NVDA
  može prouzročiti reprodukciju zvukova greške zbog promjena u dodatku.

## Verzija 18.03

* Zahtijeva NVDA 2018.1.
* Budući da NVDA 2018.1 dolazi s potvrdnim okvirom za tipkanje dodirom, taj
  potvrdni okvir više nije uključen u ovaj dodatak.

## Verzija 17.12

* Zahtijeva NVDA 2017.4. Konkretno, ovaj dodatak sada podržava mijenjenje
  konfiguracijskih profila.
* S obzirom da NVDA verzija 2017.4 uključuje izvještavanje o orijentaciji
  ekrana, ova značajka više nije dio ovog dodatka.
* Dodan skriveni potvrdni okvir u dijaloškom okviru Interakcija dodirom,
  koji kompletno onemogućava podršku dodirom (dostupno je, ako su
  konfiguracijski profili aktivni koji nemaju uobičajenu konfiguraciju).
* Ako se koristi NVDA 2018.1, dijaloški okvir „Interakcija dodirom” biti će
  prikazan dvaput u podizborniku NVDA postavki. Druga stavka je dijaloški
  okvir koji dolazi s dodatkom.
* U dijaloškom okviru Interakcija dodirom ovog dodatka, modus tipkanja
  dodirom više se ne prikazuje, ako koristite nedavno objavljene razvojne
  verzije NVDA.

## Verzija 17.10

* Zbog Microsoft pravila za podršku, Windows 8 (originalno izdanje) više
  nije podržan.
* NVDA više neće dvaput izvještavati o orijentaciji ekrana tijekom
  korištenja razvojnih verzija NVDA 2017.4.

## Verzija 17.07.1

* U dijaloškom okviru interakcije dodirom, dodana je opcija za ručno
  uključivanje i isključivanje proslijeđivanja dodirne naredbe bez upotrebe
  štoperice.
* Ako je ručno isključen modus proslijeđivanja, te ako je isti uključen
  prije nego što modusu proslijeđivanja istekne vrijeme, interakcija dodirom
  biti će aktivirana.

## Verzija 17.07

* Dodan je novi dijaloški okvir pod nazivom „Interakcija dodirom” u
  podizborniku NVDA postavki za definiranje načina rada NVDA čitača s
  ekranima osjetljivim na dodir.
* Nakon instaliranja ove verzije, prilikom pritiskanja tipki na dodirnoj
  tipkovnici, željena tipka se mora dodirnuti dvaput. Moguće je prebaciti se
  na stari način rada, aktiviranjem tipkanja dodirom u dijaloškom okviru
  Interakcija dodirom.
* Dodana je naredba (nedodijeljena) koja dozvoljava NVDA čitaču ignorirati
  dodirne geste u intervalu do 10 sekundi.
* Dodana je opcija u dijaloškom okviru interakcije dodirom koja dozvoljava
  NVDA čitaču zaustaviti interakciju dodirom u intervalu između 3 i 10
  sekundi, kako bi se direktno izvršile dodirne geste (kad NVDA nije
  pokrenut; standardno je 5 sekundi).
* Dodane su poruke za otkrivanje grešaka tijekom izvođenja desnog klika
  (dodirni i zadrži) i njihovo spremanje u NVDA log (zahtijeva NVDA verziju
  2017.1 ili noviju).
* Zbog promjena u reproduciranju koordinata ekrana, zahtijeva NVDA verziju
  2017.1 ili noviju.

##Verzija 17.03

* Riješen problem gdje se pri izvještavanju koordinata nije čuo zvuk ili se
  pojavljivao zvuk pogreške tijekom korištenja NVDA verzije 2017.1 ili
  novije.

##Verzija 16.12

* Dodirni modus za web radi u programu Microsoft Edge, Microsoft Word i
  drugdje gdje je moguće koristiti modus pretraživanja.
* Dodani su popisi i orijentiri za elemente u dodirnom modusu za web.

## Verzija 16.06

* Inicijalna stabilna verzija.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
