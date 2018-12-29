# coding=utf8

import hashlib
import random
import datetime

seje = {}

def kriptiraj_geslo(geslo, sol):
    return hashlib.sha256((geslo + str(sol)).encode()).hexdigest()

def generiraj_sejo(uporabnisko_ime):
    rnd = random.randint(1, 100000000)
    kljuc = uporabnisko_ime + str(rnd) + str(datetime.datetime.now())
    
    id = hashlib.sha256(kljuc.encode()).hexdigest()
    
    global seje
    seje[id] = uporabnisko_ime
    
    return id

def vrni_uporabnika_iz_seje(id):
    global seje
    if id in seje:
        return seje[id]
    
    return None