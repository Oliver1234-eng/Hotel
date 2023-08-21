def sortiranje_liste_rezervacija(lista_rezervacija):
    return sorted(lista_rezervacija, key = lambda rezervacija: rezervacija['korisnik'])

def dodavanje_nove_rezervacije(lista_rezervacija, nova_rezervacija):
    lista_rezervacija.append(nova_rezervacija)

    return True

def zaglavlje():
    print("id    |hotel          |sobe           |datum kreiranja|datum prijave  |datum odjave   |korisnik       |status         ")
    print("-----------------------------------------------------------------------------------------------------------------------")

def prikaz_rezervacija(rezervacija):
    print(str(rezervacija['id']).ljust(6) + "|" + rezervacija['hotel'].ljust(15)[:15] + "|" +rezervacija['sobe'].ljust(15)[:15] + "|" + str(rezervacija['dan kreiranja']).ljust(2) + "." + str(rezervacija['mesec kreiranja']).ljust(2) + "." + str(rezervacija['godina kreiranja']).ljust(2) + ".    |" + str(rezervacija['dan prijave']).ljust(2) + "." + str(rezervacija['mesec prijave']).ljust(2) + "." + str(rezervacija['godina prijave']).ljust(2) + ".    |" + str(rezervacija['dan odjave']).ljust(2) + "." + str(rezervacija['mesec odjave']).ljust(2) + "." + str(rezervacija['godina odjave']).ljust(2) + ".    |" + rezervacija['korisnik'].ljust(15) + "|" + rezervacija['status'].ljust(15)[:15])

def prikaz_svih_rezervacija(lista_rezervacija):
    for rezervacija in lista_rezervacija:
        prikaz_rezervacija(rezervacija)

def prikaz_svih_zavrsenih_rezervacija(lista_rezervacija):
    for rezervacija in lista_rezervacija:
        if rezervacija['status'] == 'zavrsena' and rezervacija['korisnik'] == 'pera':
            prikaz_rezervacija(rezervacija)

def prikaz_svih_nezapocetih_rezervacija(lista_rezervacija):
    for rezervacija in lista_rezervacija:
        if rezervacija['status'] == 'nije zapoceta' and rezervacija['korisnik'] == 'pera':
            prikaz_rezervacija(rezervacija)

def prikaz_svih_u_toku_rezervacija(lista_rezervacija):
    for rezervacija in lista_rezervacija:
        if rezervacija['status'] == 'u toku' and rezervacija['korisnik'] == 'pera':
            prikaz_rezervacija(rezervacija)

def kombinovana_pretraga_po_datumu_kreiranja(lista_rezervacija, dan_kreiranja, mesec_kreiranja, godina_kreiranja):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if (dan_kreiranja == str(rezervacija['dan kreiranja'])) and (mesec_kreiranja == str(rezervacija['mesec kreiranja'])) and (godina_kreiranja == str(rezervacija['godina kreiranja'])):
            ret_val.append(rezervacija)
    
    return ret_val

def kombinovana_pretraga_po_datumu_prijave(lista_rezervacija, dan_prijave, mesec_prijave, godina_prijave):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if (dan_prijave == str(rezervacija['dan prijave'])) and (mesec_prijave == str(rezervacija['mesec prijave'])) and (godina_prijave == str(rezervacija['godina prijave'])):
            ret_val.append(rezervacija)
    
    return ret_val

def kombinovana_pretraga_po_datumu_odjave(lista_rezervacija, dan_odjave, mesec_odjave, godina_odjave):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if (dan_odjave == str(rezervacija['dan odjave'])) and (mesec_odjave == str(rezervacija['mesec odjave'])) and (godina_odjave == str(rezervacija['godina odjave'])):
            ret_val.append(rezervacija)
    
    return ret_val

def pronalazenje_po_korisniku(lista_rezervacija, deo_korisnika):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if deo_korisnika.lower() in rezervacija['korisnik'].lower():
            ret_val.append(rezervacija)
    
    return ret_val

def pronalazenje_po_statusu(lista_rezervacija, deo_statusa):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if deo_statusa.lower() in rezervacija['status'].lower():
            ret_val.append(rezervacija)
    
    return ret_val

def kombinovana_pretraga(lista_rezervacija, dan_kreiranja, mesec_kreiranja, godina_kreiranja, dan_prijave, mesec_prijave, godina_prijave, dan_odjave, mesec_odjave, godina_odjave, korisnik, status):
    ret_val = []
    for rezervacija in lista_rezervacija:
        if (dan_kreiranja == str(rezervacija['dan kreiranja'])) or (mesec_kreiranja == str(rezervacija['mesec kreiranja'])) or (godina_kreiranja == str(rezervacija['godina kreiranja'])) or (dan_prijave == str(rezervacija['dan prijave'])) or (mesec_prijave == str(rezervacija['mesec prijave'])) or (godina_prijave == str(rezervacija['godina prijave'])) or (dan_odjave == str(rezervacija['dan odjave'])) or (mesec_odjave == str(rezervacija['mesec odjave'])) or (godina_odjave == str(rezervacija['godina odjave'])) or (korisnik == rezervacija['korisnik']) or (status == rezervacija['status']):
            ret_val.append(rezervacija)
    
    return ret_val