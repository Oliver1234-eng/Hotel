def sortiranje_liste_soba(lista_soba):
    return sorted(lista_soba, key = lambda soba: soba['tip'])

def zaglavlje():
    print("id    |hotel          |broj sobe      |broj kreveta   |tip            |klima          |tv            |cena           ")
    print("---------------------------------------------------------------------------------------------------------------------")

def prikaz_soba(soba):
    print(str(soba['id']).ljust(6) + "|" + soba['hotel'].ljust(15)[:15] + "|" + str(soba['broj sobe']).ljust(15) + "|" + str(soba['broj kreveta']).ljust(15) + "|" + soba['tip'].ljust(15) + "|" + soba['klima'].ljust(15) + "|" + soba['tv'].ljust(15) + "|" + str(soba['cena']).ljust(15))

def prikaz_svih_soba(lista_soba):
    for soba in lista_soba:
        prikaz_soba(soba)

def pronalazenje_po_broju_sobe(lista_soba, deo_broja_sobe):
    ret_val = []
    for soba in lista_soba:
        if deo_broja_sobe == str(soba['broj sobe']):
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_broju_sobe_za_izmenu(lista_soba, deo_broja_sobe):
    ret_val = []
    for soba in lista_soba:
        if deo_broja_sobe == str(soba['broj sobe']):
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_broju_kreveta(lista_soba, deo_broja_kreveta):
    ret_val = []
    for soba in lista_soba:
        if deo_broja_kreveta == str(soba['broj kreveta']):
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_tipu(lista_soba, deo_tipa):
    ret_val = []
    for soba in lista_soba:
        if deo_tipa.lower() in soba['tip'].lower():
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_klimi(lista_soba, deo_klime):
    ret_val = []
    for soba in lista_soba:
        if deo_klime.lower() in soba['klima'].lower():
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_tvu(lista_soba, deo_tva):
    ret_val = []
    for soba in lista_soba:
        if deo_tva.lower() in soba['tv'].lower():
            ret_val.append(soba)
    
    return ret_val

def pronalazenje_po_ceni(lista_soba, deo_cene):
    ret_val = []
    for soba in lista_soba:
        if deo_cene == str(soba['cena']):
            ret_val.append(soba)
    
    return ret_val

def kombinovana_pretraga(lista_soba, broj_sobe, broj_kreveta, deo_tipa, deo_klime, deo_tva, cena):
    ret_val = []
    for soba in lista_soba:
        if (broj_sobe == str(soba['broj sobe'])) or (broj_kreveta == str(soba['broj kreveta'])) or (deo_tipa.lower() in soba['tip'].lower()) or (deo_klime.lower() in soba['klima'].lower()) or (deo_tva.lower() in soba['tv'].lower()) or (cena == str(soba['cena'])):
            ret_val.append(soba)
    
    return ret_val

def dodavanje_nove_sobe(lista_soba, nova_soba):
    lista_soba.append(nova_soba)

    return True

def pronalazenje_po_broju_sobe_za_izmenu(lista_soba, broj_sobe):
    for soba in lista_soba:
        if str(soba['broj sobe']) == str(broj_sobe):
            return soba
    
    return None

def izmena_podataka_o_sobi(lista_soba, broj_sobe, tip, klima, tv):
    soba = pronalazenje_po_broju_sobe_za_izmenu(lista_soba, broj_sobe)
    soba['tip'] = tip
    soba['klima'] = klima
    soba['tv'] = tv

    return soba