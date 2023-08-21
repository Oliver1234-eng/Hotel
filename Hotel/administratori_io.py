import citanje_cuvanje

def str_2_administrator(str_administrator):
    podaci = str_administrator.split(',')
    
    return {'id': int(podaci[0]), 'korisnicko ime': podaci[1], 'lozinka': podaci[2], 'ime': podaci[3], 
    'prezime': podaci[4], 'telefon': podaci[5], 'email': podaci[6], 'uloga': podaci[7], 
    'obrisan': podaci[8] == 'True'}

def citanje_liste_administratora():
    return citanje_cuvanje.citanje_liste('administratori.txt', str_2_administrator)