# coding=utf8

from bottle import get, post, redirect, run, template, request, response, static_file
import random
import bottle
from datetime import datetime
import modeli
from modeli import Uporabnik
import pomozne

bottle.TEMPLATE_PATH.insert(0, './pogledi')

@get('/slike/<pot:re:.*\.(jpg|png)>')
def slike(pot):
    return static_file(pot, root='slike')

@get('/assets/<pot:re:.*\.(js|css)>')
def slike(pot):
    return static_file(pot, root='assets')

@get('/')
def indeks():
    pomozne.vrni_sejo()
    minDate = date.today().strftime('%Y, %m - 1, %d')

    lokacije = modeli.vrni_lokacije()
    return template('indeks', lokacije = lokacije, minDate = minDate)

@get('/registracija')
def registracija():
    pomozne.vrni_sejo()
    return template('registracija')

@post('/registracija')
def registracija_post():
    pomozne.vrni_sejo()

    geslo = request.forms.get('geslo')
    potrditev = request.forms.get('potrditev')
    if geslo != potrditev:
        return template('registracija')

    ime = request.forms.get('ime')
    priimek = request.forms.get('priimek')
    uporabnisko_ime = request.forms.get('uporabnisko_ime')
    email = request.forms.get('email')
    stevilka_osebne = request.forms.get('stevilka_osebne')

    sol = random.randint(1, 100000000)
    prijavni_zeton = pomozne.kriptiraj_geslo(geslo, sol)

    modeli.dodaj_uporabnika(ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol, Uporabnik.NAVADEN)

    return template('registracija')

@get('/prijava')
def prijava():
    pomozne.vrni_sejo()
    return template('prijava')

@post('/prijava')
def prijava_post():
    pomozne.vrni_sejo()

    uporabnisko_ime = request.forms.get('uporabnisko_ime')
    uporabnik = modeli.podatki_uporabnika(uporabnisko_ime)

    if uporabnik == None:
        return template('prijava')

    zeton = pomozne.kriptiraj_geslo(request.forms.get('geslo'), uporabnik['sol'])

    if uporabnik['prijavni_zeton'] != zeton:
        return template('prijava')

    pomozne.dodaj_uporabnika_v_sejo(uporabnisko_ime)

    if uporabnik['tip'] == Uporabnik.ADMINISTRATOR:
        return redirect('/admin')

    return redirect('/')

@post('/izbira_kolesa')
def izbira_kolesa():
    pomozne.vrni_sejo()

    format = '%Y-%m-%dT%H:%M:%S.%fZ'
    lokacija = request.forms.get('lokacija')
    od = datetime.strptime(request.forms.get('datum_od'), format).date()
    do = datetime.strptime(request.forms.get('datum_do'), format).date()

    kolesa = modeli.vrni_kolesa()

    return template('izbira_kolesa', kolesa = kolesa)

@get('/admin')
def admin():
    pomozne.vrni_sejo()

    uporabnisko_ime = pomozne.vrni_uporabnika_iz_seje()
    uporabnik = modeli.podatki_uporabnika(uporabnisko_ime)

    if uporabnik == None or uporabnik['tip'] != Uporabnik.ADMINISTRATOR:
        return redirect('/')

    return template('admin')

run(reloader=True, debug=True)
