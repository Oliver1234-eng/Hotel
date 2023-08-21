def prijava(lista_recepcionera, korisnicko_ime, lozinka):
    for recepcioner in lista_recepcionera:
        if korisnicko_ime == recepcioner['korisnicko ime'] and lozinka == recepcioner['lozinka']:
            return recepcioner

    return None

def zaglavlje():
    print("id    |ime            |prezime        |korisnicko ime |email          |uloga          |hotel          ")
    print("------------------------------------------------------------------------------------------------------")

def prikaz_recepcionera(recepcioner):
    print(str(recepcioner['id']).ljust(6) + "|" + recepcioner['ime'].ljust(15)[:15] + "|" + recepcioner['prezime'].ljust(15)[:15] + "|" + recepcioner['korisnicko ime'].ljust(15)[:15] + "|" + recepcioner['email'].ljust(15)[:15] + "|" + recepcioner['uloga'].ljust(15) + "|" + recepcioner['hotel'].ljust(15))

def prikaz_svih_recepcionera(lista_recepcionera):
    for recepcioner in lista_recepcionera:
        prikaz_recepcionera(recepcioner)

def dodavanje_novog_recepcionera(lista_recepcionera, novi_recepcioner):
    for recepcioner in lista_recepcionera:
        if recepcioner['korisnicko ime'] == novi_recepcioner['korisnicko ime']:
            return False
    lista_recepcionera.append(novi_recepcioner)

    return True

def pronalazenje_po_korisnickom_imenu_za_brisanje(lista_recepcionera, korisnicko_ime):
    for recepcioner in lista_recepcionera:
        if recepcioner['korisnicko ime'] == korisnicko_ime:
            return recepcioner
    
    return None

def brisanje_recepcionera(lista_recepcionera, korisnicko_ime):
    recepcioner_za_brisanje = pronalazenje_po_korisnickom_imenu_za_brisanje(lista_recepcionera, korisnicko_ime)
    if recepcioner_za_brisanje:
        recepcioner_za_brisanje['obrisan'] = True
        return True

    return False

def pronalazenje_po_imenu(lista_recepcionera, deo_imena):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_imena.lower() in recepcioner['ime'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def pronalazenje_po_prezimenu(lista_recepcionera, deo_prezimena):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_prezimena.lower() in recepcioner['prezime'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def pronalazenje_po_korisnickom_imenu(lista_recepcionera, deo_korisnickog_imena):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_korisnickog_imena.lower() in recepcioner['korisnicko ime'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def pronalazenje_po_emailu(lista_recepcionera, deo_emaila):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_emaila.lower() in recepcioner['email'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def pronalazenje_po_ulozi(lista_recepcionera, deo_uloge):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_uloge.lower() in recepcioner['uloga'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def pronalazenje_po_hotelu(lista_recepcionera, deo_hotela):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if deo_hotela.lower() in recepcioner['hotel'].lower():
            ret_val.append(recepcioner)
    
    return ret_val

def kombinovana_pretraga(lista_recepcionera, deo_imena, deo_prezimena, deo_korisnickog_imena, deo_emaila, deo_uloge, deo_hotela):
    ret_val = []
    for recepcioner in lista_recepcionera:
        if (deo_imena.lower() in recepcioner['ime'].lower()) or (deo_prezimena.lower() in recepcioner['prezime'].lower()) or (deo_korisnickog_imena.lower() in recepcioner['korisnicko ime'].lower()) or (deo_emaila.lower() in recepcioner['email'].lower()) or (deo_uloge.lower() in recepcioner['uloga'].lower()) or (deo_hotela.lower() in recepcioner['hotel'].lower()):
            ret_val.append(recepcioner)
    
    return ret_val