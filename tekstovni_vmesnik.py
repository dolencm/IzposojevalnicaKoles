import getpass
import modeli

def izberi_moznost(moznosti):
    # Izbira možnosti iz menuja
    for i, moznost in enumerate(moznosti, 1):
        print("%2i) %s" % (i, moznost))

    while True:
        izbira = input('Vnesite izbiro: ')
        if izbira.isdigit():
            n = int(izbira)
            if 1 <= n <= len(moznosti):
                return n

def dodaj_uporabnika():
    # Vnos podatkov o uporabniku
    print('Vnesi podatke o uporabniku')
    ime = input('Ime: ')
    priimek = input('Priimek: ')
    uporabnisko_ime = input('Uporabniško ime: ')
    email = input('Email: ')
    stevilka_osebne = input('Številka osebne izkaznice: ')
    
    geslo = getpass.getpass('Geslo: ')
    geslo2 = getpass.getpass('Ponovi geslo: ')
    if geslo != geslo2:
        print('Gesli se ne ujemata!')
        return False
    
    modeli.dodaj_uporabnika(ime, priimek, email, stevilka_osebne, uporabnisko_ime, geslo)
    return True
    
def izpisi_uporabnike():
    # Izpis podatkov o uporabnikih
    print('Podatki o uporabnikih')
    uporabniki = modeli.vrni_uporabnike()
    for i in range(len(uporabniki)):
        if i > 0 and i % 25 == 0:
            naprej = input('Naprej (D/N)? ')
            if naprej.upper() != 'D':
                break

        uporabnik = uporabniki[i]
        print("%3i Ime: %s Priimek: %s Uporabniško ime: %s" %
            (uporabnik[0], uporabnik[1], uporabnik[2], uporabnik[5]))
        print("    Email: %s" % (uporabnik[3]))

def dodaj_kolo():
    # Dodaj novo kolo v bazo
    print('Vnesi podatke o kolesu')
    tip = input('Tip: ')
    znamka = input('Znamka: ')
    model = input('Model: ')
    lokacija = int(input('Lokacija: '))
    serijska_stevilka = input('Serijska stevilka: ')
    velikost = input('Velikost okvirja: ')

    modeli.dodaj_kolo(velikost, serijska_stevilka, tip, znamka, model, '', lokacija)

def izpis_koles():
    lokacija = int(input('Izberi lokacijo: '))

    # Izpis podatkov o vseh kolesih na lokaciji
    print('Podatki o kolesih na lokaciji')
    kolesa = modeli.vrni_kolesa_na_lokaciji(lokacija)
    for i in range(len(kolesa)):
        if i > 0 and i % 25 == 0:
            naprej = input('Naprej (D/N)? ')
            if naprej.upper() != 'D':
                break

        kolo = kolesa[i]
        print("%3i Tip: %s Znamka: %s Model: %s Velikost: %s" % (kolo[0], kolo[3], kolo[4], kolo[5], kolo[1]))

def pokazi_moznosti():
    # Prikaži menu
    print(50 * '-')
    izbira = izberi_moznost([
        'dodaj uporabnika',
        'izpisi uporabnike',
        'dodaj kolo',
        'izpisi kolesa',
        'izhod'
    ])

    if izbira == 1:
        dodaj_uporabnika()
    elif izbira == 2:
        izpisi_uporabnike()
    elif izbira == 3:
        dodaj_kolo()
    elif izbira == 4:
        izpis_koles()
    elif izbira == 5:
        exit()

def main():
    print("Izposojevalnica koles")
    while True:
        pokazi_moznosti()

main()
