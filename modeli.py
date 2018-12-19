# coding=utf8

import sqlite3
import hashlib
import random
import baza

conn = sqlite3.connect('izposojevalnica.db')
conn.execute('PRAGMA foreign_keys = ON')
baza.ustvari_bazo_ce_ne_obstaja(conn)

def dodaj_uporabnika(ime, priimek, email, stevilka_osebne, uporabnisko_ime, geslo):
    # Doda novega uporabnika v tabelo uporabnik
    sol = random.randint(1, 100000000)
    prijavni_zeton = hashlib.sha256((geslo + str(sol)).encode()).hexdigest()
    
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
        SELECT
            id, ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol
        FROM
            uporabniki
    """).fetchall()

def podatki_uporabnika(uporabnisko_ime, geslo):
    # Prebere podatke za danim uporabniškim imenom
    uporabnik = conn.execute("""
        SELECT
            id, ime, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol
        FROM
            uporabniki
        WHERE
            uporabnisko_ime = ?
    """, [uporabnisko_ime]).fetchall()

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
        SELECT
            id, velikost, serijska_stevilka, tip, znamka, model, slika
        FROM
            kolesa
        WHERE
            lokacija = ?
    """, [lokacija]).fetchall()

def commit():
    # Shrani stanje baze
    conn.commit()
