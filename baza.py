# coding=utf8

import csv
import random
import pomozne

def pobrisi_tabele(conn):
    # Pobriše vse tabele iz baze
    conn.execute("DROP TABLE IF EXISTS uporabniki")
    conn.execute("DROP TABLE IF EXISTS kolesa")
    conn.execute("DROP TABLE IF EXISTS lokacije")
    conn.execute("DROP TABLE IF EXISTS rezervacije")
    conn.execute("DROP TABLE IF EXISTS izposoje")

def ustvari_tabele(conn):
    # Tabela naših uporabnikov
    conn.execute("""
        CREATE TABLE uporabniki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ime VARCHAR NOT NULL,
            priimek VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            stevilka_osebne INTEGER NOT NULL,
            uporabnisko_ime VARCHAR NOT NULL,
            prijavni_zeton VARCHAR NOT NULL,
            sol INTEGER NOT NULL,
            tip INTEGER NOT NULL
        )
    """)
    
    # Tabela kolesa, ki jih imamo
    conn.execute("""
        CREATE TABLE kolesa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            velikost VARCHAR NOT NULL,
            serijska_stevilka VARCHAR NOT NULL,
            tip VARCHAR NOT NULL,
            znamka VARCHAR NOT NULL,
            model VARCHAR NOT NULL,
            slika VARCHAR NOT NULL,
            lokacija INTEGER REFERENCES lokacije(id)
        )
    """)
    
    # Tabela vseh naših lokacij kjer oddajamo kolesa
    conn.execute("""
        CREATE TABLE lokacije (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naslov VARCHAR NOT NULL,
            posta INTEGER NOT NULL,
            kraj VARCHAR NOT NULL,
            zemljepisna_sirina REAL NOT NULL,
            zemljepisna_dolzina REAL NOT NULL
        )
    """)
    
    # Tabela rezervacij
    conn.execute("""
        CREATE TABLE rezervacije (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum_od DATE NOT NULL,
            datum_do DATE NOT NULL,
            kolo INTEGER REFERENCES kolesa(id),
            lokacija INTEGER REFERENCES lokacije(id),
            uporabnik INTEGER REFERENCES uporabnik(id)
        )
    """)
    
    # Tabela izposojenih koles
    conn.execute("""
        CREATE TABLE izposoje (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum_od DATE NOT NULL,
            datum_do DATE NOT NULL,
            status INTEGER NOT NULL,
            kolo INTEGER REFERENCES kolesa(id),
            lokacija INTEGER REFERENCES lokacije(id),
            uporabnik INTEGER REFERENCES uporabniki(id)
        )
    """)

def uvozi_uporabnike(conn):
    # Uvozi uporabnike
    with open('podatki/uporabniki.csv', encoding='utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)

        poizvedba = """
            INSERT INTO uporabniki VALUES ({})
        """.format(', '.join(["?"] * (len(stolpci) - 1)))
        for vrstica in podatki:
            sol = random.randint(1, 100000000)
            vrstica[6] = pomozne.kriptiraj_geslo(vrstica[9], sol)
            vrstica[7] = sol
            del vrstica[9]
            conn.execute(poizvedba, vrstica)

def uvozi_lokacije(conn):
    # Uvozi lokacije
    with open('podatki/lokacije.csv', encoding='utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)

        poizvedba = """
            INSERT INTO lokacije VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_kolesa(conn):
    # Uvozi kolesa
    with open('podatki/kolesa.csv', encoding='utf-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        
        poizvedba = """
            INSERT INTO kolesa VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def ustvari_bazo(conn):
    # Postavi bazo
    pobrisi_tabele(conn)
    ustvari_tabele(conn)

    uvozi_uporabnike(conn)
    uvozi_lokacije(conn)
    uvozi_kolesa(conn)

def ustvari_bazo_ce_ne_obstaja(conn):
    # Ustvari bazo, če ta še ne obstaja
    with conn:
        cur = conn.execute("select count(*) from sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)
