RAPORT 3 PROTOYP (w trakcie realizacji)

CO ZROBIŁEM:

1. Umożliwiłem dodawanie wierszy do tabeli miejsca(forms.py, routes.py, pliki HTML)
2. Umożliwiłem dodawanie wierszy do tabeli osoby(forms.py, routes.py, pliki HTML)
3. Wyświatlanie wszystkich wierszy z tabel typy urzadzen i urzadzenia CRUD -> R (Read)
4. Umożliwienie dodawania wierszy do tabeli typy urzadzen (forms.py, routes.py, pliki HTML)
5. TODO: Umożliwienie dodawania wierszy do tabeli  urzadzenia(forms.py, routes.py, pliki HTML)
CO PLANUJE ZROBIĆ:

========================================================================

RAPORT 2

CO ZROBIŁEM:

1. Utworzenie pliku startowego run.py
2. Utworzenie modelu obiektowego bazy danych w pliku models.py, SQLAlchemy
3. Utworzenie pliku routes.py. Za jepo pomocą sterujemy przechodzimy do poszczególnych podstron.
4. W wyposazenie/templates umieściłem pliki html, takie jak: about.html, dodaj_miejsce.html, pokaz_miejsca.html, pokaz_miejsce.html, pokaz_osoby.html
   w których będzie realizowane wyświatlnie potrzebnych informacji. W pliku layout.html umieszczona jest część wspólna dla wyświetlanych stron 
5. W katalogu wyposazenie/static umieściłem plik main.css
6. Wygenerowanie pliku (pip freeze > requirements.txt) requirements w którym zawarta jest informacja o użytych modułach.

CO PLANUJE ZROBIĆ:

1. W kolejnych krokach planuje wykonanie pliku forms.py, który obsługuje wtforms.
2. Bedę rozszerzał katalog templates o dodatkowe pliki html, w których realizowana będzie dalsza funkcjonalność programu i stowarzyszony plik routes.py,
   który będzie obsługiwał/zarządzał te pliki.

========================================================================

RAPORT 1 (założenia)

Aplikacja do utrzymywania informacji o sprzęcie przekazanym pracownikom.
Zastosowane technologie:
- Python
- SqlAlchemy
- Flask

Aplikacja bedzie obslugiwana w przegladarce internetowej - za to odpowiedzialny bedzie Flask ( https://python101.readthedocs.io/pl/latest/webflask/ )

Informacje bedą przechowywane w bazie danych. Wybrałem bazę danych SQLite.
Komunikacja pomiedzy baza danych a resztą aplikacji bedzie wykonywana poprzez ORM SQLAlchemy a dokladnie jego odmianę ktora zaimplementowana jest we Flasku.

Będzie można wprowadzic informacje o nowym sprzecie, przypisac do niego osobę, bedzie mozna wpisywać informacje o nowych osobach.
Sprzet bedzie mial takze mozliwosć  przypisania go do jakiego typu urzadzeń należy i te typy takze bedzie mozna wpisywać np ze sprzet pendrive nalezy do typu urzadzeń dyski.
Najpierw w Git stworzymy swoje repozytorium.
Nastepnie za pomocą pythona tworze projekt i jego strukturę tzn nazwę i jakie bedzie miał pliki i co w jakich plikach bede programować.
 
Nastepnie Kolejna rzecz to za pomoca pythona i za pomocą modulu SQLAlchemy będę  tworzyć model tabeli bazy danych tak by aplikacja wiedziała jak wyglada baza danych i aby za pomoca aplikacji mozna stworzyć bazę danych i pozniej z nia sie komunikowac, tzn zapisywac, odczytywac, aktualizowac, usuwac tzw. operacje CRUD (Create, Read, Update, Delete).