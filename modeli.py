# coding=utf8

import sqlite3
import baza

conn = sqlite3.connect('izposojevalnica.db')
conn.execute('PRAGMA foreign_keys = ON')
baza.ustvari_bazo_ce_ne_obstaja(conn)

def dictionary_factory(cur, row):
    dict = {}
    for idx, col in enumerate(cur.description):
        dict[col[0]] = row[idx]
    return dict

conn.row_factory = dictionary_factory

def dodaj_uporabnika(ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol):
    # Doda novega uporabnika v tabelo uporabnik
    with conn:
        conn.execute("""
            INSERT INTO uporabniki
                (ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
        """, [ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol])

def vrni_uporabnike():
    # Vrne seznam uporabnike
    return conn.execute("""
        SELECT * FROM uporabniki
    """).fetchall()

def podatki_uporabnika(uporabnisko_ime):
    # Prebere podatke za danim uporabniškim imenom
    return conn.execute("""
        SELECT * FROM uporabniki WHERE uporabnisko_ime = ?
    """, [uporabnisko_ime]).fetchone()

def dodaj_kolo(velikost, serijska_stevilka, tip, znamka, model, slika, lokacija):
    # Doda novo kolo na lokacijo
    with conn:
        conn.execute("""
            INSERT INTO kolesa
                (velikost, serijska_stevilka, tip, znamka, model, slika, lokacija)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
        """, [velikost, serijska_stevilka, tip, znamka, model, slika, lokacija])

def vrni_kolesa_na_lokaciji(lokacija):
    # Vrne podatke o kolesih na lokaciji
    return conn.execute("""
        SELECT * FROM kolesa WHERE lokacija = ?
    """, [lokacija]).fetchall()

def commit():
    # Shrani stanje baze
    conn.commit()
