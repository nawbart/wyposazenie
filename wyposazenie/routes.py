from flask import render_template, url_for, flash, redirect, request
from wyposazenie import app, db
from wyposazenie.forms import DodajMiejsceForm, DodajOsobeForm, DodajTypUrzadzeniaForm
from wyposazenie.models import Miejsca, Osoby, TypyUrzadzen, Urzadzenia


@app.route("/")
@app.route("/home")
def home():
    mq = Miejsca.query.all()
    return render_template('home.html', miejsca=mq)

# ========= MIEJSCA ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "miejsca".
@app.route("/pokazmiejsca")
def pokazmiejsca():
    miejsca_query = Miejsca.query.all()
    return render_template('pokaz_miejsca.html', miejsca=miejsca_query)


# READ, wyswietla jeden wybrany rekord z tablicy "miejsca"
@app.route("/pokazmiejsce/<int:id_miejsce>", methods=['GET', 'POST'])
def pokaz_miejsce(id_miejsce):
    miejsce_query = Miejsca.query.get_or_404(id_miejsce)
    return render_template("pokaz_miejsce.html", miejsce = miejsce_query )

# CREATE, dodaj miejsce
@app.route("/miejsce/new", methods=['GET', 'POST'])
def dodajmiejsce():
    #tworze obiekt form ktory pochodzi z klasy forms.dadajMiejsceForm
    form = DodajMiejsceForm()
    #jesli nacisnieto przycisk submit
    if form.validate_on_submit():
        #tworze obiekt wiersz_miejsce za pomoca konstruktora Miejsce z models
        wiersz_miejsce = Miejsca(nazwa=form.nazwa.data, opis=form.opis.data)
        #dwie ponizsze linie to robie takiego inserta za pomoca sqlalchemy
        db.session.add(wiersz_miejsce)
        db.session.commit()
        # pokazuje komunikat jesli wszystko bedzie ok
        flash(f'Dodano nowy wiersz do tabeli bazy danych.')
        # przechodze do strony pokaz miejsca gdzie widac wszstkie miejsca
        return redirect(url_for('pokazmiejsca'))
    return render_template('dodaj_miejsce.html', title='Dodaj miejsce', form=form,
                           legend="Dodaj miejce")


# ========= OSOBY ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "osoby"
@app.route("/pokazosoby")
def pokazosoby():
    osoby_query = Osoby.query.all()
    return render_template('pokaz_osoby.html', osoby = osoby_query)

# CREATE, dodaj osobe
@app.route("/osoba/new", methods=['GET', 'POST'])
def dodajosobe():
    #tworze obiekt form ktory pochodzi z klasy forms.dadajMiejsceForm
    form = DodajOsobeForm()
    #jesli nacisnieto przycisk submit
    if form.validate_on_submit():
        #tworze obiekt wiersz_osoba za pomoca konstruktora Osoby z models.py
        wiersz_osoba = Osoby(imie=form.imie.data, nazwisko=form.nazwisko.data, email=form.email.data,
                             opis=form.opis.data)
        #dwie ponizsze linie to robie takiego inserta za pomoca sqlalchemy
        db.session.add(wiersz_osoba)
        db.session.commit()
        # pokazuje komunikat jesli wszystko bedzie ok
        flash(f'Dodano nowy wiersz do tabeli bazy danych.')
        # przechodze do strony pokaz osoby gdzie widac wszstkie osoby
        return redirect(url_for('pokazosoby'))
    return render_template('dodaj_osobe.html', title='Dodaj osobe', form=form,
                           legend="Dodaj osobe")


# ========= TYPYURZADZEN ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "typy urzadzen"
@app.route("/pokaztypyurzadzen")
def pokaztypyurzadzen():
    typyurzadzen_query = TypyUrzadzen.query.all()
    return render_template('pokaz_typyurzadzen.html', typyurzadzen=typyurzadzen_query)

# CREATE, dodaj typy urzadzen
@app.route("/typurzadzenia/new", methods=['GET', 'POST'])
def dodajtypurzadzenia():
    #tworze obiekt form ktory pochodzi z klasy forms.dodajTypUrzadzeniaForm
    form = DodajTypUrzadzeniaForm()
    #jesli nacisnieto przycisk submit
    if form.validate_on_submit():
        #tworze obiekt wiersz_typurzadzenia za pomoca konstruktora TypyUrzadzen z models.py
        wiersz_typurzadzenia = TypyUrzadzen(nazwa=form.nazwa.data, opis=form.opis.data)
        #dwie ponizsze linie to robie takiego inserta za pomoca sqlalchemy
        db.session.add( wiersz_typurzadzenia)
        db.session.commit()
        # pokazuje komunikat jesli wszystko bedzie ok
        flash(f'Dodano nowy wiersz do tabeli bazy danych.')
        # przechodze do strony pokaz typyurzadzen gdzie widac wszstkie typyurzadzen
        return redirect(url_for('pokaztypyurzadzen'))
    return render_template('dodaj_typurzadzenia.html', title='Dodaj typ urzadzenia', form=form,
                           legend="Dodaj typ urzadzenia")


# ========= URZADZENIA ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "urzadzenia"
@app.route("/pokazurzadzenia")
def pokazurzadzenia():
    urzadzenia_query = Urzadzenia.query.all()
    return render_template('pokaz_urzadzenia.html', urzadzenia=urzadzenia_query)
