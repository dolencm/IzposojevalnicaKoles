# coding=utf8

from bottle import get, post, redirect, run, template, request, response
import random
import bottle
import modeli
import pomozne

bottle.TEMPLATE_PATH.insert(0, './pogledi')

@get('/')
def indeks():
    id = request.get_cookie('seja')
    uporabnisko_ime = pomozne.vrni_uporabnika_iz_seje(id)
    uporabnik = modeli.podatki_uporabnika(uporabnisko_ime)
    return template('indeks', ime = uporabnik['ime'], priimek = uporabnik['priimek'])

@get('/registracija')
def registracija():
    return template('registracija')
    
@post('/registracija')
def registracija_post():
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
    
    modeli.dodaj_uporabnika(ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol)
    
    return template('registracija')
    
@get('/prijava')
def prijava():
    return template('prijava')
    
@post('/prijava')
def prijava_post():
    uporabnisko_ime = request.forms.get('uporabnisko_ime')
    uporabnik = modeli.podatki_uporabnika(uporabnisko_ime)

    if uporabnik == None:
        return template('prijava')
    
    zeton = pomozne.kriptiraj_geslo(request.forms.get('geslo'), uporabnik['sol'])
    
    if uporabnik['prijavni_zeton'] != zeton:
        return template('prijava')

    id = pomozne.generiraj_sejo(uporabnisko_ime)
    response.set_cookie('seja', id)
    return redirect('/')

run(reloader=True, debug=True)