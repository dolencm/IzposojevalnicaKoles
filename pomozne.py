# coding=utf8

from bottle import request, response
import hashlib
import random
import datetime

seje = {}

def kriptiraj_geslo(geslo, sol):
    return hashlib.sha256((geslo + str(sol)).encode()).hexdigest()

def vrni_sejo():
    global seje

    id = request.get_cookie('seja')
    if id not in seje:
        rnd = random.randint(1, 100000000)
        kljuc = str(rnd) + str(datetime.datetime.now())

        id = hashlib.sha256(kljuc.encode()).hexdigest()
        seje[id] = {}
        response.set_cookie('seja', id)

    return id

def dodaj_uporabnika_v_sejo(uporabnik):
    global seje
    seje[vrni_sejo()]['uporabnik'] = uporabnik

def vrni_uporabnika_iz_seje():
    global seje

    seja = seje[vrni_sejo()]
    if 'uporabnik' in seja:
        return seja['uporabnik']
    
    return None

def dodaj_podatke_v_sejo(paket):
    global seje

    seje[vrni_sejo()]['podatki'] = paket

def vrni_podatke_iz_seje():
    global seje

    id = vrni_sejo()
    if id in seje:
        return seje[id]['podatki']
    return None