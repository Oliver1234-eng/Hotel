def zaglavlje():
    print("id    |realizovane rezervacije  |izdate sobe    |ukupna zarada  |prosecna ocena |vrsta          ")
    print("------------------------------------------------------------------------------------------------")

def prikaz_izvestaja(izvestaj):
    print(str(izvestaj['id']).ljust(6) + "|" + str(izvestaj['realizovane rezervacije']).ljust(25) + "|" + str(izvestaj['izdate sobe']).ljust(15) + "|" + str(izvestaj['ukupna zarada']).ljust(15) + "|" + str(izvestaj['prosecna ocena']).ljust(15) + "|" + izvestaj['vrsta'].ljust(15))

def prikaz_dnevnih_izvestaja(lista_izvestaja):
    for izvestaj in lista_izvestaja:
        if izvestaj['vrsta'] == 'dnevni':
            prikaz_izvestaja(izvestaj)

def prikaz_svih_izvestaja(lista_izvestaja):
    for izvestaj in lista_izvestaja:
        prikaz_izvestaja(izvestaj)

def prikaz_nedeljnih_izvestaja(lista_izvestaja):
    for izvestaj in lista_izvestaja:
        if izvestaj['vrsta'] == 'nedeljni':
            prikaz_izvestaja(izvestaj)

def prikaz_mesecnih_izvestaja(lista_izvestaja):
    for izvestaj in lista_izvestaja:
        if izvestaj['vrsta'] == 'mesecni':
            prikaz_izvestaja(izvestaj)

def dodavanje_dnevnog_izvestaja(lista_izvestaja, novi_izvestaj):
    lista_izvestaja.append(novi_izvestaj)

    return True

def dodavanje_nedeljnog_izvestaja(lista_izvestaja, novi_izvestaj):
    lista_izvestaja.append(novi_izvestaj)

    return True

def dodavanje_mesecnog_izvestaja(lista_izvestaja, novi_izvestaj):
    lista_izvestaja.append(novi_izvestaj)

    return True