from wyposazenie import db

#modeluje strukture bazy danych w sqlAlchemy, to jest potrzebne przy stworzeniu bazy danych
#oraz przy interakcji z bazą danych, czyli w zapytaniach (np.select, update, insert)

class Miejsca(db.Model):
    #na sztywno wymuszam,zeby tablica nazywala się MIEJSCA
    __tablename__ = "miejsca"

    #Tworze w tablicy pole/kolumna o nazwie ID_MIEJSCA typu int i PK (primary key)
    id_miejsce = db.Column(db.Integer, primary_key = True)

    # Tworze w tablicy pole/kolumna o nazwie NAZWA typu str(30), niepusty i unikalny
    nazwa = db.Column(db.String(30), nullable = False, unique = True)

    # Tworze w tablicy pole/kolumna o nazwie OPIS typu str(150)
    opis = db.Column(db.String(150))


class Osoby(db.Model):
    __tablename__ = "osoby"

    id_osoba = db.Column(db.Integer, primary_key = True)
    imie = db.Column(db.String(30), nullable = False)
    nazwisko = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30))
    opis = db.Column(db.String(150))

class TypyUrzadzen(db.Model):
    __tablename__ = "typy_urzadzen"

    id_typ_urzadzenia = db.Column(db.Integer, primary_key = True)
    nazwa = db.Column(db.String(30), nullable=False, unique = True)
    opis = db.Column(db.String(150))

class Urzadzenia(db.Model):
    id_urzadzenie = db.Column(db.Integer, primary_key = True)
    nr_seryjny = db.Column(db.String(60))
    nazwa_urzadzenia = db.Column(db.String(60), unique = True)
    id_miejsce = db.Column(db.Integer, db.ForeignKey("miejsca.id_miejsce"), nullable = False)
    id_osoba = db.Column(db.Integer, db.ForeignKey("osoby.id_osoba"), nullable=False)
    opis = db.Column(db.String(150))
    id_typ_urzadzenia = db.Column(db.Integer, db.ForeignKey("typy_urzadzen.id_typ_urzadzenia"), nullable=False)