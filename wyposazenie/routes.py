from flask import render_template, url_for, flash, redirect, request
from wyposazenie import app, db
from wyposazenie.forms import DodajMiejsceForm
from wyposazenie.models import Miejsca, Osoby


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
    form = DodajMiejsceForm()
    if form.validate_on_submit():
        wiersz_miejsce = Miejsca(nazwa=form.nazwa.data, opis=form.opis.data)
        db.session.add(wiersz_miejsce)
        db.session.commit()
        flash(f'Dodano nowy wiersz do tabeli bazy danych.')
        return redirect(url_for('pokazmiejsca'))
    return render_template('dodaj_miejsce.html', title='Dodaj miejsce', form=form,
                           legend="Dodaj miejce")


# ========= OSOBY ====================================================
# READ, wyswietla wszystkie rokordy z tabeli "osoby"
@app.route("/pokazosoby")
def pokaz_osoby():
    osoby_query = Osoby.query.all()
    return render_template('pokaz_osoby.html', osoby = osoby_query)




