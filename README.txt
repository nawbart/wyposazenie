RAPORT 2




RAPORT 1

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