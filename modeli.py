# coding=utf8

import sqlite3
import baza
import enum
import pomozne

class Uporabnik(enum.IntEnum):
    NAVADEN = 0
    ADMINISTRATOR = 1

class Izposoja(enum.IntEnum):
    AKTIVNA = 0
    ZAKLJUCENA = 1

conn = sqlite3.connect('izposojevalnica.db')
conn.execute('PRAGMA foreign_keys = ON')
baza.ustvari_bazo_ce_ne_obstaja(conn)

def dictionary_factory(cur, row):
    dict = {}
    for idx, col in enumerate(cur.description):
        dict[col[0]] = row[idx]
    return dict

conn.row_factory = dictionary_factory

def dodaj_uporabnika(ime, lokacija, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol, tip):
    # Doda novega uporabnika v tabelo uporabnik
    with conn:
        conn.execute("""
            INSERT INTO uporabniki
                (ime, lokacija, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol, tip)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [ime, lokacija, priimek, email, stevilka_osebne, uporabnisko_ime, prijavni_zeton, sol, int(tip)])

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

def vrni_kolesa(od, do):
    # Vrne vse podatke o vseh kolesih
    return conn.execute("""
        SELECT * FROM kolesa WHERE
            id NOT IN (
                SELECT kolo
                FROM rezervacije
                WHERE datum_od <= ? AND ? <= datum_do
                    OR datum_od <= ? AND ? <= datum_do
                    OR ? <= datum_od AND ? >= datum_do)
            and id NOT IN (
                SELECT kolo
                FROM izposoje
                WHERE status = 0 AND datum_od <= ? AND ? <= datum_do
                    OR datum_od <= ? AND ? <= datum_do
                    OR ? <= datum_od AND ? >= datum_do)
    """, [od, od, do, do, od, do, od, od, do, do, od, do]).fetchall()

def vrni_lokacije():
    # Vrne podatke o vseh lokacijah
    return conn.execute("""
        SELECT * FROM lokacije
    """).fetchall()

def vrni_lokacijo(id):
    # Vrne podatke o lokaciji
    return conn.execute("""
        SELECT * FROM lokacije WHERE id = ?
    """, [id]).fetchone()

def vrni_rezervacije(id):
    # Vrne rezervacije na lokaciji
    return conn.execute("""
        SELECT
            r.id, r.datum_od, r.datum_do, u.ime, u.priimek, u.stevilka_osebne,
            k.znamka, k.model, k.serijska_stevilka, l.naziv, k.id as kolo, l.id as lokacija
        FROM
            rezervacije r
            join kolesa k on r.kolo = k.id
            join uporabniki u on r.uporabnik = u.id
            join lokacije l on k.lokacija = l.id
        WHERE
            r.lokacija = ?
        ORDER BY
            r.datum_od asc
    """, [id]).fetchall()

def vrni_izposoje(id):
    # Vrne izposojena kolesa na lokaciji
    return conn.execute("""
        SELECT
            i.id, i.datum_od, i.datum_do, u.ime, u.priimek, u.stevilka_osebne,
            k.znamka, k.model, k.serijska_stevilka
        FROM
            izposoje i
            join kolesa k on i.kolo = k.id
            join uporabniki u on i.uporabnik = u.id
        WHERE
            i.lokacija = ? and status = ?
        ORDER BY
            i.datum_do asc
    """, [id, Izposoja.AKTIVNA]).fetchall()

def dodaj_rezervacijo(datum_od, datum_do, kolo, lokacija, uporabnik):
    # Ustvari rezervacijo kolesa za uporabnika
    with conn:
        conn.execute("""
            INSERT INTO rezervacije
                (datum_od, datum_do, kolo, lokacija, uporabnik)
            VALUES
                (?, ?, ?, ?, ?)
        """, [datum_od, datum_do, kolo, lokacija, uporabnik])

def izposodi_rezervacijo(id, datum):
    # Izposodi rezervirano kolo
    with conn:
        rez = conn.execute("""
            SELECT * FROM rezervacije WHERE id = ?
        """, [id]).fetchone()
        conn.execute("""
            DELETE FROM rezervacije WHERE id = ?
        """, [id])
        conn.execute("""
            INSERT INTO izposoje
                (datum_od, datum_do, status, kolo, lokacija, uporabnik)
            VALUES
                (?, ?, ?, ?, ?, ?)
        """, [datum, rez['datum_do'], Izposoja.AKTIVNA, rez['kolo'], rez['lokacija'], rez['uporabnik']])

def zakljuci_izposojo(id, datum):
    # Označi izposojo za zaključeno
    with conn:
        conn.execute("""
            UPDATE izposoje SET status = ?, datum_do = ? WHERE id = ?
        """, [Izposoja.ZAKLJUCENA, datum, id])

def prestavi_kolo(id, loc):
    # Prestavi kolo na novo lokacijo
    with conn:
        conn.execute("""
            UPDATE kolesa SET lokacija = ? WHERE id = ?
        """, [loc, id])

def statistika(loc):
    # Vrne podatke o zaključenih izposojah na lokaciji
    return conn.execute("""
            SELECT
                i.datum_od, i.datum_do, k.znamka, k.model, u.ime, u.priimek
            FROM
                izposoje i
                join kolesa k on i.kolo = k.id
                join uporabniki u on i.uporabnik = u.id
            WHERE
                i.lokacija = ? AND i.status = ?
            ORDER BY
                i.datum_od DESC
        """, [loc, Izposoja.ZAKLJUCENA]).fetchall()