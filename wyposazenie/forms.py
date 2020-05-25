from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField,\
    IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from wyposazenie.models import Miejsca, Osoby, TypyUrzadzen, Urzadzenia

#dodaje formularz wtfforms do obslugi wprowadzania informacji o nowych miejscach
class DodajMiejsceForm(FlaskForm):
    #tworze pole "nazwa" w ktorym zapisywac bede zawartosc pola "nazwa" z tab. Miejsca
    #DataRequired w validators zapewnia, ze w polu nazwa musze cos wpisac
    nazwa = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])

    # tworze pole "opis" w ktorym zapisywac bede zawartosc pola "opis" z tab. Miejsca
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])

    #tworzenie przycisku
    submit = SubmitField("Dodaj miejsce")

    # aby przed dodaniem rekordu do bazy sprawdzac czy wartosc pola unikalnego nie została ponownie wpisana
    # tworzymy taką funkcje sprawdzającą dla pola nazwa
    def validate_nazwa(self, nazwa):
        miejsce_query = Miejsca.query.filter_by(nazwa=nazwa.data).first()
        if miejsce_query:
            raise ValidationError("Ta nazwa miejsca jest już wykorzystana, wprowadź inną: ")


class UpdateMiejsceForm(FlaskForm):
    nazwa = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])

    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])

    submit = SubmitField("Zaktualizuj miejsce")

    def validate_nazwa(self, nazwa):
        miejsce_query = Miejsca.query.filter_by(nazwa=nazwa.data).first()
        if miejsce_query:
            raise ValidationError("Ta nazwa miejsca jest już wykorzystana, wprowadź inną: ")

class DodajOsobeForm(FlaskForm):

    imie = StringField("Imie", validators=[DataRequired(), Length(min=3, max=30)])
    nazwisko = StringField("Nazwisko", validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField("Email", validators=[Email()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Dodaj osobe")

class UpdateOsobaForm(FlaskForm):

    imie = StringField("Imie", validators=[DataRequired(), Length(min=3, max=30)])
    nazwisko = StringField("Nazwisko", validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField("Email", validators=[Email()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Zaktualizuj osobe")

class DodajTypUrzadzeniaForm(FlaskForm):

    nazwa = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Dodaj typ urzadzenie")

    # aby przed dodaniem rekordu do bazy sprawdzac czy wartosc pola unikalnego nie została ponownie wpisana
    # tworzymy taką funkcje sprawdzającą dla pola nazwa
    def validate_nazwa(self, nazwa):
        typurzadzenia_query = TypyUrzadzen.query.filter_by(nazwa=nazwa.data).first()
        if typurzadzenia_query:
            raise ValidationError("Ta nazwa typu urządzenia jest już wykorzystana, wprowadź inną: ")

class UpdateTypUrzadzeniaForm(FlaskForm):

    nazwa = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Zaktualizuj typ urzadzenia")

    # aby przed dodaniem rekordu do bazy sprawdzac czy wartosc pola unikalnego nie została ponownie wpisana
    # tworzymy taką funkcje sprawdzającą dla pola nazwa
    def validate_nazwa(self, nazwa):
        typurzadzenia_query = TypyUrzadzen.query.filter_by(nazwa=nazwa.data).first()
        if typurzadzenia_query:
            raise ValidationError("Ta nazwa typu urządzenia jest już wykorzystana, wprowadź inną: ")



class DodajUrzadzenieForm(FlaskForm):

    nazwa_urzadzenia = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    nr_seryjny = StringField("Nr. seryjny", validators=[DataRequired(), Length(min=3, max=60)])
    id_miejsce = IntegerField("ID_miejsce", validators=[DataRequired()])
    id_osoba = IntegerField("ID_osoba", validators=[DataRequired()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    id_typ_urzadzenia = IntegerField("ID_typ_urzadzenia", validators=[DataRequired()])

    submit = SubmitField("Dodaj typ urzadzenie")

    # aby przed dodaniem rekordu do bazy sprawdzac czy wartosc pola unikalnego nie została ponownie wpisana
    # tworzymy taką funkcje sprawdzającą dla pola nazwa
    def validate_nazwa_urzadzenia(self, nazwa_urzadzenia):
        nazwa_urzadzenia_query = Urzadzenia.query.filter_by(nazwa_urzadzenia=nazwa_urzadzenia.data).first()
        if nazwa_urzadzenia_query:
            raise ValidationError("Ta nazwa urządzenia jest już wykorzystana, wprowadź inną: ")

class UpdateUrzadzenieForm(FlaskForm):

    nazwa_urzadzenia = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    nr_seryjny = StringField("Nr. seryjny", validators=[DataRequired(), Length(min=3, max=60)])
    id_miejsce = IntegerField("ID_miejsce", validators=[DataRequired()])
    id_osoba = IntegerField("ID_osoba", validators=[DataRequired()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    id_typ_urzadzenia = IntegerField("ID_typ_urzadzenia", validators=[DataRequired()])

    submit = SubmitField("Zaktualizuj typ urzadzenia")

    # aby przed dodaniem rekordu do bazy sprawdzac czy wartosc pola unikalnego nie została ponownie wpisana
    # tworzymy taką funkcje sprawdzającą dla pola nazwa
    def validate_nazwa_urzadzenia(self, nazwa_urzadzenia):
        nazwa_urzadzenia_query = Urzadzenia.query.filter_by(nazwa_urzadzenia=nazwa_urzadzenia.data).first()
        if nazwa_urzadzenia_query:
            raise ValidationError("Ta nazwa urządzenia jest już wykorzystana, wprowadź inną: ")