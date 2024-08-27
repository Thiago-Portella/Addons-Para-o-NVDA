# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Pobierz [wersja stabilna][1]
* Zgodność z NVDA: 2022.4 i nowsze

Ten dodatek udostępnia gesty dotykowe dla NVDA oraz zestaw specjalnych
gestów do łatwiejszej nawigacji w trybie czytania.

Uwaga: ten dodatek wymaga NVDA 2022.3 lub nowszego działającego na
komputerze z ekranem dotykowym i systemem Windows 10 lub 11.

## Polecenia

### Dostępne wszędzie

* Podwójne stuknięcie czterema palcami: przełącza pomoc wprowadzania.
* Przesunięcie w prawo czterema palcami: Przełączanie klawiatury dotykowej
  (za zwyczaj ją włącza).
* Przesunięcie dwoma palcami w lewo: przełączanie dyktowania (Windows+H;
  Windows 10 w wersji 1709 lub nowszej).

### Tryb obiektu

* Przesunięcie w dół trzema palcami: odczytanie bieżącego okna.
* Przesunięcie w lewo trzema palcami: odczytaj obiekt posiadający fokus..
* Przesunięcie w prawo trzema palcami: odczytaj bieżący obiekt nawigacyjny.
* Przesunięcie w górę czterema palcami: odczytaj tytuł bieżącego okna.
* Przesunięcie w dół czterema palcami: odczytaj tekst paska stanu.

## Tryb dotykowy w Internecie

Ten tryb gestów, dostępny w trybie czytania, pozwala nawigować po wybranych
elementach dokumentu. Aby przełączyć się w ten tryb z dokumentów trybu
czytania, wykonaj stuknięcie trzema palcami. W tym trybie, Przesunięcie w
górę lub w dół jednym palcem przełącza między dostępnymi sposobami
nawigacji, Przesunięcie jednym palcem w lewo lub prawo przenosi do
poprzedniego lub następnego wybranego elementu. Po wyjściu z dokumentu trybu
czytania, używany jest obiektowy tryb gestów dotykowych.

## Tryb dotykowej zmiany ustawień syntezatora

Możesz użyć tego trybu do szybkiej zmiany ustawień syntezatora, np. by
wybrać głos, albo zmienić głośność. Przesuń dwoma palcami w lewo lub prawo
aby przechodzić między ustawieniami. Przesuń dwoma palcami w górę lub w dół
aby zmieniać wartości danego ustawienia. Gesty te odpowiadają klawiszom
szybkiej zmiany ustawień syntezatora.

## Wersja 23.02

* Wymagana jest NVDA 2022.4 lub nowsza.
* Wymagany jest system Windows 10 21H2 (aktualizacja z listopada 2021
  r./kompilacja 19044) lub nowszy.

## Wersja 23.01

* Wymagana jest NVDA 2022.3 lub nowsza.
* System Windows 10 lub nowszy jest wymagany, ponieważ system Windows 8.1
  nie jest już obsługiwany przez firmę Microsoft od stycznia 2023 r.
* Możliwe jest ponowne przypisanie klawiatury dotykowej i poleceń dyktowania
  z okna dialogowego gestów wprowadzania w kategorii Ulepszone gesty
  dotykowe.
* Usunięto obejście stanu tylko do odczytu dla klawiatury dotykowej,
  ponieważ jest ono rozwiązane w systemie Windows 10.

## Wersja 22.03

* Wymagana jest nvda 2021.3 lub nowsza.
* Podczas próby zainstalowania dodatku w systemie Windows 7, 8 i 8.1
  zostanie wyświetlony komunikat ostrzegawczy.

## Wersja 21.10

* NVDA 2021.2 lub nowsza jest wymagana ze względu na zmiany w NVDA, które
  mają wpływ na ten dodatek.

## Wersja 21.08

* Początkowa obsługa systemu Windows 11.

## Wersja 21.01

* Wymagana jest wersja NVDA 2020.3 lub nowsza.
* W systemie Windows 10 w wersji 1709 lub nowszej przesunięcie dwoma palcami
  w lewo spowoduje przełączenie dyktowania (Windows+ H).
* Usuń dedykowane polecenie przełączania obsługi interakcji dotykowych z
  dodatku.
* Ponieważ obsługa interakcji dotykowych może być przełączana z panelu
  ustawień interakcji dotykowych NVDA, usunięto dedykowany panel ustawień
  ulepszonych gestów dotykowych.

## Wersja 20.04

* Usunięto możliwość wyłączenia przez NVDA interakcji dotykowej na okres do
  dziesięciu sekund (przejście polecenia dotykowego).
* Usunięto funkcję sygnału dźwiękowego ogłaszania współrzędnych.

## Wersja 20.07

* Dodano polecenie klawiatury umożliwiające przełączanie interakcji
  dotykowej lub włączanie/wyłączanie przechodzenia dotykowego
  (Control+Alt+NVDA+T).
* Ponieważ NVDA 2020.1 i nowsze zawierają polecenie dotykowe do wykonywania
  kliknięć prawym przyciskiem myszy (dotknięcie i przytrzymanie jednym
  palcem), polecenie zostało usunięte z tego dodatku. W rezultacie wymagana
  jest NVDA 2020.1 lub nowsza.
* Możliwość wyłączenia przez NVDA interakcji dotykowej na okres do
  dziesięciu sekund (przekazywanie poleceń dotykowych) jest przestarzała. W
  przyszłości ta funkcja będzie przełączać interakcję dotykową.
* W migawkach programistycznych NVDA, ze względu na zmiany funkcji
  interakcji dotykowej, funkcja przekazywania poleceń dotykowych i panel
  ustawień ulepszonych gestów dotykowych zostaną wyłączone. Polecenie użyte
  do włączenia przekazywania poleceń dotykowych przełączy interakcję
  dotykową.
* Funkcja sygnału dźwiękowego ogłaszania współrzędnych jest przestarzała i
  zostanie usunięta w przyszłej wersji dodatku.
* Sygnał dźwiękowy komunikatu współrzędnych nie będzie słyszalny podczas
  korzystania z klawiatury dotykowej.
* NVDA nie będzie już wydawać się nic robić ani odtwarzać dźwięków błędów
  podczas eksploracji nowoczesnych funkcji wejściowych, takich jak panel
  emoji za pomocą dotyku.
* NVDA wyświetli komunikat o błędzie, jeśli nie można aktywować klawiatury
  dotykowej (przesunięcie palcem w prawo czterema palcami).

## Wersja 20.06

* Naprawiono niektóre błędy stylistyczne związane z kodem,  a także
  naprawiono błędy związane z linterem Flake8.

## Wersja 20.04

* Polecenie prawego przycisku myszy (stuknięcie z przytrzymaniem jednym
  palcem) jest wbudowane w NVDA w wersji 2020.1.

## Wersja 20.01

* Wymagana jest wersja NVDA 2019.3 lub nowsza.
* Polecenie do przełączania trybu dotykowego (włączając w to dotykowe
  przełączanie) nie będzie więcej funkcjonowało, gdy wsparcie dotykowe jest
  kompletnie wyłączone.

## Wersja 19.11

* Dodano komunikaty pomocy dla dodatkowych poleceń dotykowych.

## Wersja 19.09

* Wsparcie dotykowe może być wyłączone z jakiegokolwiek miejsca, czyli nie
  tylko przy aktywnym normalnym profilu.

## Wersja 19.07

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Wersja 18.12

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Wersja 18.08

* Zgodne z NVDA 2018.3 i nowszymi.

## Wersja 18.06

* Od teraz ustawienia dodatku znajdują się w nowym, wielopanelowym oknie
  ustawień NVDA, w kategorii "Enhanced Touch Gestures" . Z powodu licznych
  zmian, wymagana jest wersja NVDA 2018.2.
* Naprawiono problemy zgodności z wxPython 4.

## Wersja 18.04

* Rozwiązuje problem, przez który kategoria reakcji na dotyk w panelu
  ustawień NVDA może wywoływać dźwięki błędu, z powodu zmian wprowadzonych w
  tym dodatku.

## Wersja 18.03

* Wymaga NVDA 2018.1.
* NVDA 2018.1 posiada już pole wyboru, które włącza wpisywanie dotykowe,
  dlatego zostało ono usunięte z dodatku.

## Wersja 17.12

* Wymaga NVDA 2017.4. Przede wszystkim, dodatek może już przełączać się
  między profilami.
* Ponieważ NVDA 2017.4 może ogłaszać orientację ekranu, usunięto tę funkcję
  z dodatku.
* Aby zupełnie wyłączyć wsparcie dotyku, Do dialogu reakcji na dotyk dodano
  ukryte pole wyboru, dostępne tylko wtedy gdy aktywny jest inny profil niż
  standardowy.
* W przypadku korzystania z NVDA 2018.1 lub nowszego okno dialogowe
  Interakcja dotykowa zostanie wyświetlone dwukrotnie w menu preferencji
  NVDA. Drugim elementem jest okno dialogowe dołączone do dodatku.
* W oknie dialogowym reakcji dotykowej dodatku, od wersji NVDA 2018.1 tryb
  wpisywania dotykowego nie jest już pokazywany.

## Wersja 17.10

* W związku z polityką wsparcia firmy Microsoft, Windows 8 nie jest już
  wspierany.
* NVDA nie będzie już dwukrotnie ogłaszać orientacji ekranu w wersjach
  rozwojowych  NVDA 2017.4.

## Wersja 17.07.1

* Do dialogu reakcji na dotyk dodano opcję służącą do ręcznego przełączania
  przepuszczania dotyku bez potrzeby użycia timera.
* Jeśli ręczny tryb przepuszczania jest wyłączony a przepuszczanie dotyku
  zostało włączone zanim wygasł jego czas, włączy się reakcja na dotyk.

## Wersja 17.07

* Do Meni Ustawień NVDA dodano okno dialogowe reakcji na dotyk. Służy ono do
  konfigurowania sposobu w jaki NVDA współpracuje z ekranami dotykowymi.
* Po instalacji tej wersji dodatku trzeba dwukrotnie stuknąć w żądany
  klawisz na klawiaturze dotykowej. Do poprzedniego sposobu można powrócić
  włączając wpisywanie dotykowe w oknie reakcji na dotyk.
* Dodano funkcję nieprzypisanego polecenia, dzięki której NVDA ignoruje
  gesty dotykowe przez czas do 10 sekund.
* Do okna dialogowego reakcji na dotyk dodano opcję, która pozwala NVDA
  wstrzymać reakcję na dotyk od 3 do 10 sekund. Dzięki temu można wykonywać
  gesty na ekranie dotykowym jakgdyby screenreader w ogóle nie był
  uruchomiony. Domyślna wartość wynosi 5 sekund.
* Dodano zapisywanie wiadomości debugowania w dzienniku NVDA podczas
  wykonywania prawego kliknięcia (stuknięcie i przytrzymanie). Wymagana
  wersja NVDA 2017.1 lub nowsza.
* W związku ze zmianami w odtwarzaniu współrzędnych ekranu, wymagana jest
  wersja NVDA 2017.1 lub nowsza.

##Version 17,03

* Poprawiono błąd, z powodu którego dźwięk oznajmiania położenia nie był
  odtwarzany lub zamiast niego pojawiał się dźwięk błędu. Działo się to w
  NVDA 2017.1 i nowszych.

##Version 16,12

* Dotykowy tryb czytania działa w Microsoft Edge, Microsoft Word i innych
  programach, gdzie używa się trybu przeglądu.
* Do elementów dotykowego trybu czytania dodano listy i punkty orientacyjne.

## Wersja 16.06

* Pierwsza wersja stabilna.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
