import citanje_cuvanje

def recepcioner_2_str(recepcioner):
    return str(recepcioner['id']) + ',' + recepcioner['korisnicko ime'] + ',' + recepcioner['lozinka'] + ',' + recepcioner['ime'] + ',' + recepcioner['prezime'] + ',' + recepcioner['telefon'] + ',' + recepcioner['email'] + ',' + recepcioner['uloga'] + ',' + str(recepcioner['obrisan']) + ',' + recepcioner['hotel']

def str_2_recepcioner(str_recepcioner):
    podaci = str_recepcioner.split(',')
    
    return {'id': int(podaci[0]), 'korisnicko ime': podaci[1], 'lozinka': podaci[2], 'ime': podaci[3], 
    'prezime': podaci[4], 'telefon': podaci[5], 'email': podaci[6], 'uloga': podaci[7], 
    'obrisan': podaci[8] == 'True', 'hotel': podaci[9]}

def cuvanje_liste_recepcionera(lista_recepcionera):
    citanje_cuvanje.cuvanje_liste(lista_recepcionera, 'recepcioneri.txt', recepcioner_2_str)

def citanje_liste_recepcionera():
    return citanje_cuvanje.citanje_liste('recepcioneri.txt', str_2_recepcioner)

def sledeci_id():
    f_recepcioneri = open('recepcioneri.txt', 'r')
    lines = f_recepcioneri.readlines()
    f_recepcioneri.close()
    
    return len(lines) + 1