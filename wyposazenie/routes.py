from flask import render_template, url_for, flash, redirect, request
from wyposazenie import app, db
from wyposazenie.forms import DodajMiejsceForm, DodajOsobeForm, DodajTypUrzadzeniaForm,\
    DodajUrzadzenieForm, UpdateMiejsceForm, UpdateOsobaForm, UpdateTypUrzadzeniaForm
from wyposazenie.models import Miejsca, Osoby, TypyUrzadzen, Urzadzenia


@app.route("/")
@app.route("/home")
def home():
    # mq = Miejsca.query.all()
    # return render_template('home.html', miejsca=mq)
    urzadzenia_query = Urzadzenia.query.all()
    return render_template('pokaz_urzadzenia.html', urzadzenia=urzadzenia_query)

# ========= MIEJSCA ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "miejsca".
@app.route("/pokazmiejsca")
def pokazmiejsca():
    miejsca_query = Miejsca.query.all()
    return render_template('pokaz_miejsca.html', miejsca=miejsca_query)

# # READ, to show one record
# @app.route("/container/<int:container_id>", methods=['GET', 'POST'])
# def onecontainer(container_id):
#     # daj container z tym id ale jesli nie ma tego id to zwroc 404 co oznacza ze strona nie istnieje.
#     container_q = Containers.query.get_or_404(container_id)
#     return render_template("container.html", container=container_q)

# READ, wyswietla jeden wybrany rekord z tablicy "miejsca"
@app.route("/pokazmiejsce/<int:id_miejsce>", methods=['GET', 'POST'])
def pokazmiejsce(id_miejsce):
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

# UPDATE, aktualizujemy wybrany wiersz z tabeli miejsca
@app.route("/miejsce/<int:id_miejsce>/update", methods=["GET", "POST"])
def update_miejsce(id_miejsce):
    miejsce_query = Miejsca.query.get_or_404(id_miejsce)
    form = UpdateMiejsceForm()
    if form.validate_on_submit():
        #po nacisnieciu przycisku dane z forms.py sa kopiowane do miejsce_query
        # i nastepnie sa commitowane do bazy
        miejsce_query.nazwa = form.nazwa.data
        miejsce_query.opis = form.opis.data
        db.session.commit()
        # pokauje komunikat, ze sie udalo
        flash("miejsce zostalo zaktualizowane", "success")
        #powrot do pokaz_miejsce
        return redirect(url_for("pokazmiejsce", id_miejsce=miejsce_query.id_miejsce))
    #jesli chcemy byc pewni ze wypelnienie formy bylo przeprowadzone po żądaniu GET
    elif request.method == "GET":
        #te dwie linie wypelniaja formy wybranymi wartosciami z wybranego wiersza
        form.nazwa.data = miejsce_query.nazwa
        form.opis.data = miejsce_query.opis
    return render_template("dodaj_miejsce.html", title="Update Miejsca", form=form,
                           legend="Update Miejsca")

# DELETE miejsce
@app.route("/miejsce/<int:id_miejsce>/delete", methods=["POST"])
def delete_miejsce(id_miejsce):
    #sprawdza czy istnieje pobrany id_miejsce w bazie danych, jeśli nie ma to wykonuje sie metoda
    # .get_or_404(...)
    miejsce_query = Miejsca.query.get_or_404(id_miejsce, f"Nie ma danego wiersza z id{id_miejsce}"
                                                                f" w tabeli miejsca.")
    #sprawdza czy id_miejsce nie bylo wykorzystane w tabeli urzadzenia
    urzadzenie_query = Urzadzenia.query.filter_by(id_miejsce=id_miejsce).first()
    # jesli id_miejsce bylo wykorzystane w tabeli urzadzenia to nie mozna usunac wiersza.
    if urzadzenie_query:
        flash(f"Ten wiersz nie moze byc usuniety! Zostal uzyty w tabeli urzadzenia,"
              f" id :{urzadzenie_query.id_miejsce}.","danger")
    # w przeciwnym wypadku usuniecie jest mozliwe:
    else:
        db.session.delete(miejsce_query)
        db.session.commit()
        flash("Twoje miejsce zostalo usuniete", "success")
    return redirect(url_for("pokazmiejsca"))


# ========= OSOBY ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "osoby"
@app.route("/pokazosoby")
def pokazosoby():
    osoby_query = Osoby.query.all()
    return render_template('pokaz_osoby.html', osoby = osoby_query)

# READ, wyswietla jeden wybrany rekord z tablicy "osoby"
@app.route("/pokazosobe/<int:id_osoba>", methods=['GET', 'POST'])
def pokazosobe(id_osoba):
    osoba_query = Osoby.query.get_or_404(id_osoba)
    return render_template("pokaz_osobe.html", osoba = osoba_query )


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

# UPDATE, aktualizujemy wybrany wiersz z tabeli osoby
@app.route("/osoba/<int:id_osoba>/update", methods=["GET", "POST"])
def update_osoba(id_osoba):
    osoba_query = Osoby.query.get_or_404(id_osoba)
    form = UpdateOsobaForm()
    if form.validate_on_submit():
        #po nacisnieciu przycisku dane z forms.py sa kopiowane do osoba_query
        # i nastepnie sa commitowane do bazy
        osoba_query.nazwisko = form.nazwisko.data
        osoba_query.opis = form.opis.data
        osoba_query.imie = form.imie.data
        osoba_query.email = form.email.data
        db.session.commit()
        # pokauje komunikat, ze sie udalo
        flash("Osoba zostala zaktualizowana", "success")
        #powrot do pokaz_osoba
        return redirect(url_for("pokazosobe", id_osoba=osoba_query.id_osoba))
    #jesli chcemy byc pewni ze wypelnienie formy bylo przeprowadzone po żądaniu GET
    elif request.method == "GET":
        #te dwie linie wypelniaja formy wybranymi wartosciami z wybranego wiersza
        form.nazwisko.data = osoba_query.nazwisko
        form.opis.data = osoba_query.opis
        form.imie.data = osoba_query.imie
        form.email.data = osoba_query.email
    return render_template("dodaj_osobe.html", title="Update Osoby", form=form,
                           legend="Update Osoby")

# DELETE osoba
@app.route("/osoba/<int:id_osoba>/delete", methods=["POST"])
def delete_osoba(id_osoba):
    #sprawdza czy istnieje pobrany id_osoba w bazie danych, jeśli nie ma to wykonuje sie metoda
    # .get_or_404(...)
    osoba_query = Osoby.query.get_or_404(id_osoba, f"Nie ma danego wiersza z id{id_osoba}"
                                                                f" w tabeli osoby.")
    #sprawdza czy id_osoba nie bylo wykorzystane w tabeli urzadzenia
    urzadzenie_query = Urzadzenia.query.filter_by(id_osoba=id_osoba).first()
    # jesli id_osoba bylo wykorzystane w tabeli urzadzenia to nie mozna usunac wiersza.
    if urzadzenie_query:
        flash(f"Ten wiersz nie moze byc usuniety! Zostal uzyty w tabeli urzadzenia,"
              f" id :{urzadzenie_query.id_osoba}.","danger")
    # w przeciwnym wypadku usuniecie jest mozliwe:
    else:
        db.session.delete(osoba_query)
        db.session.commit()
        flash("Osoba zostala usunieta", "success")
    return redirect(url_for("pokazosoby"))


# ========= TYPYURZADZEN ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "typy_urzadzen"
@app.route("/pokaztypyurzadzen")
def pokaztypyurzadzen():
    typyurzadzen_query = TypyUrzadzen.query.all()
    return render_template('pokaz_typyurzadzen.html', typyurzadzen=typyurzadzen_query)

# READ, wyswietla jeden wybrany rekord z tablicy "typy_urzadzen"
@app.route("/pokaztypurzadzenia/<int:id_typ_urzadzenia>", methods=['GET', 'POST'])
def pokaztypurzadzenia(id_typ_urzadzenia):
    tu_query = TypyUrzadzen.query.get_or_404(id_typ_urzadzenia)
    return render_template("pokaz_typurzadzenia.html", typurzadzenia = tu_query )

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

# UPDATE, aktualizujemy wybrany wiersz z tabeli typy_urzadzen
@app.route("/typurzadzenia/<int:id_typ_urzadzenia>/update", methods=["GET", "POST"])
def update_typurzadzenia(id_typ_urzadzenia):
    typurzadzenia_query = TypyUrzadzen.query.get_or_404(id_typ_urzadzenia)
    form = UpdateTypUrzadzeniaForm()
    if form.validate_on_submit():
        #po nacisnieciu przycisku dane z forms.py sa kopiowane do typurzadzenia_query
        # i nastepnie sa commitowane do bazy
        typurzadzenia_query.nazwa = form.nazwa.data
        typurzadzenia_query.opis = form.opis.data
        db.session.commit()
        # pokauje komunikat, ze sie udalo
        flash("typ urzadzenia zostal zaktualizowany", "success")
        #powrot do pokaz_typurzadzenia
        return redirect(url_for("pokaztypurzadzenia", id_typ_urzadzenia=typurzadzenia_query.id_typ_urzadzenia))
    #jesli chcemy byc pewni ze wypelnienie formy bylo przeprowadzone po żądaniu GET
    elif request.method == "GET":
        #te dwie linie wypelniaja formy wybranymi wartosciami z wybranego wiersza
        form.nazwa.data = typurzadzenia_query.nazwa
        form.opis.data = typurzadzenia_query.opis
    return render_template("dodaj_typurzadzenia.html", title="Update Typ urzadzenia", form=form,
                           legend="Update Typ urzadzenia")

# DELETE typ_urzadzenia
@app.route("/typurzadzenia/<int:id_typ_urzadzenia>/delete", methods=["POST"])
def delete_typurzadzenia(id_typ_urzadzenia):
    #sprawdza czy istnieje pobrany id_typ_urzadzenia w tab. typy_urzadzen, jeśli nie ma to wykonuje sie metoda
    # .get_or_404(...)
    typurzadzenia_query = TypyUrzadzen.query.get_or_404(id_typ_urzadzenia, f"Nie ma danego wiersza z id{id_typ_urzadzenia}"
                                                                f" w tabeli osoby.")
    #sprawdza czy id_typ_urzadzenia nie bylo wykorzystane w tabeli urzadzenia
    urzadzenie_query = Urzadzenia.query.filter_by(id_typ_urzadzenia=id_typ_urzadzenia).first()
    # jesli id_typ_urzadzenia bylo wykorzystane w tabeli urzadzenia to nie mozna usunac wiersza.
    if urzadzenie_query:
        flash(f"Ten wiersz nie moze byc usuniety! Zostal uzyty w tabeli urzadzenia,"
              f" id :{urzadzenie_query.id_typ_urzadzenia}.","danger")
    # w przeciwnym wypadku usuniecie jest mozliwe:
    else:
        db.session.delete(typurzadzenia_query)
        db.session.commit()
        flash("Typ urzadzdenia zostal usuniety", "success")
    return redirect(url_for("pokaztypyurzadzen"))




# ========= URZADZENIA ====================================================
# READ, wyswietla wszystkie rekordy z tabeli "urzadzenia"
@app.route("/pokazurzadzenia")
def pokazurzadzenia():
    urzadzenia_query = Urzadzenia.query.all()
    return render_template('pokaz_urzadzenia.html', urzadzenia=urzadzenia_query)

@app.route("/urzadzenie/new", methods=['GET', 'POST'])
def dodajurzadzenie():
    #tworze obiekt form ktory pochodzi z klasy forms.dodajUrzadzenieForm
    form = DodajUrzadzenieForm()
    #jesli nacisnieto przycisk submit
    if form.validate_on_submit():
        #tworze obiekt wiersz_urzadzenie za pomoca konstruktora Urzadzenia z models.py
        wiersz_urzadzenie = Urzadzenia(nr_seryjny=form.nr_seryjny.data, nazwa_urzadzenia=form.nazwa_urzadzenia.data, id_miejsce=form.id_miejsce.data,
                                       id_osoba=form.id_osoba.data, opis=form.opis.data, id_typ_urzadzenia=form.id_typ_urzadzenia.data)
        #dwie ponizsze linie to robie takiego inserta za pomoca sqlalchemy
        db.session.add( wiersz_urzadzenie)
        db.session.commit()
        # pokazuje komunikat jesli wszystko bedzie ok
        flash(f'Dodano nowy wiersz do tabeli bazy danych.')
        # przechodze do strony pokaz urzadzenia gdzie widac wszstkie urzadzenia
        return redirect(url_for('pokazurzadzenia'))
    return render_template('dodaj_urzadzenie.html', title='Dodaj urzadzenie', form=form,
                           legend="Dodaj urzadzenie")
