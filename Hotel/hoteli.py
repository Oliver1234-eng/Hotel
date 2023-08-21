def sortiranje_liste_hotela(lista_hotela):
    return sorted(lista_hotela, key = lambda hotel: hotel['naziv'])

def zaglavlje():
    print("id    |naziv          |adresa         |bazen          |restoran       |ocena         ")
    print("-------------------------------------------------------------------------------------")

def prikaz_hotela(hotel):
    print(str(hotel['id']).ljust(6) + "|" + hotel['naziv'].ljust(15)[:15] + "|" + hotel['adresa'][:15].ljust(15) + "|" + hotel['bazen'].ljust(15) + "|" + hotel['restoran'].ljust(15) + "|" + str(hotel['ocena']).ljust(15))

def prikaz_svih_hotela(lista_hotela):
    for hotel in lista_hotela:
        prikaz_hotela(hotel)

def prikaz_najboljih_hotela(lista_hotela):
    for hotel in lista_hotela:
        if hotel['ocena'] > 3:
            prikaz_hotela(hotel)

def pronalazenje_po_nazivu(lista_hotela, deo_naziva):
    ret_val = []
    for hotel in lista_hotela:
        if deo_naziva.lower() in hotel['naziv'].lower():
            ret_val.append(hotel)
    
    return ret_val

def pronalazenje_po_adresi(lista_hotela, deo_adrese):
    ret_val = []
    for hotel in lista_hotela:
        if deo_adrese.lower() in hotel['adresa'].lower():
            ret_val.append(hotel)
    
    return ret_val

def pronalazenje_po_oceni(lista_hotela, deo_ocene):
    ret_val = []
    for hotel in lista_hotela:
        if deo_ocene == str(hotel['ocena']):
            ret_val.append(hotel)
    
    return ret_val

def kombinovana_pretraga(lista_hotela, deo_naziva, deo_adrese, ocena):
    ret_val = []
    for hotel in lista_hotela:
        if (deo_naziva.lower() in hotel['naziv'].lower()) or (deo_adrese.lower() in hotel['adresa'].lower()) or (ocena == str(hotel['ocena'])):
            ret_val.append(hotel)
    
    return ret_val

def pronalazenje_po_nazivu_za_izmenu(lista_hotela, naziv):
    for hotel in lista_hotela:
        if hotel['naziv'] == naziv:
            return hotel
    
    return None

def pronalazenje_po_nazivu_za_brisanje(lista_hotela, naziv):
    for hotel in lista_hotela:
        if hotel['naziv'] == naziv:
            return hotel
    
    return None

def dodavanje_novog_hotela(lista_hotela, novi_hotel):
    for hotel in lista_hotela:
        if hotel['naziv'] == novi_hotel['naziv']:
            return False
    lista_hotela.append(novi_hotel)

    return True

def izmena_podataka_o_hotelu(lista_hotela, naziv, sobe, bazen, restoran):
    hotel = pronalazenje_po_nazivu_za_izmenu(lista_hotela, naziv)
    hotel['sobe'] = sobe
    hotel['bazen'] = bazen
    hotel['restoran'] = restoran

    return hotel

def brisanje_hotela(lista_hotela, naziv):
    hotel_za_brisanje = pronalazenje_po_nazivu_za_brisanje(lista_hotela, naziv)
    if hotel_za_brisanje:
        hotel_za_brisanje['obrisan'] = True
        return True

    return False