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

class DodajOsobeForm(FlaskForm):

    imie = StringField("Imie", validators=[DataRequired(), Length(min=3, max=30)])
    nazwisko = StringField("Nazwisko", validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField("Email", validators=[Email()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Dodaj osobe")

class DodajTypUrzadzeniaForm(FlaskForm):

    nazwa = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    submit = SubmitField("Dodaj typ urzadzenie")

class DodajUrzadzenieForm(FlaskForm):

    nazwa_urzadzenia = StringField("Nazwa", validators=[DataRequired(), Length(min=3, max=30)])
    nr_seryjny = StringField("Nr. seryjny", validators=[DataRequired(), Length(min=3, max=60)])
    id_miejsce = IntegerField("ID_miejsce", validators=[DataRequired()])
    id_osoba = IntegerField("ID_osoba", validators=[DataRequired()])
    opis = TextAreaField("Opis", validators=[DataRequired(), Length(min=3, max=150)])
    id_typ_urzadzenia = IntegerField("ID_typ_urzadzenia", validators=[DataRequired()])

    submit = SubmitField("Dodaj typ urzadzenie")