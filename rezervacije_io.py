import citanje_cuvanje

def rezervacija_2_str(rezervacija):
    return str(rezervacija['id']) + ',' + rezervacija['hotel'] + ',' + rezervacija['sobe'] + ',' + str(rezervacija['dan kreiranja']) + ',' + str(rezervacija['mesec kreiranja']) + ',' + str(rezervacija['godina kreiranja']) + ',' + str(rezervacija['dan prijave']) + ',' + str(rezervacija['mesec prijave']) + ',' + str(rezervacija['godina prijave']) + ',' + str(rezervacija['dan odjave']) + ',' + str(rezervacija['mesec odjave']) + ',' + str(rezervacija['godina odjave']) + ',' + rezervacija['korisnik'] + ',' + rezervacija['status']  + ',' + str(rezervacija['obrisan'])

def str_2_rezervacija(str_rezervacija):
    podaci = str_rezervacija.split(',')
    
    return {'id': int(podaci[0]), 'hotel': podaci[1], 'sobe': podaci[2], 'dan kreiranja': int(podaci[3]), 
    'mesec kreiranja': int(podaci[4]), 'godina kreiranja': int(podaci[5]), 'dan prijave': int(podaci[6]), 
    'mesec prijave': int(podaci[7]), 'godina prijave': int(podaci[8]), 'dan odjave': int(podaci[9]), 
    'mesec odjave': int(podaci[10]), 'godina odjave': int(podaci[11]), 'korisnik': podaci[12], 
    'status': podaci[13], 'obrisan': podaci[14] == 'True'}

def cuvanje_liste_rezervacija(lista_rezervacija):
    citanje_cuvanje.cuvanje_liste(lista_rezervacija, 'rezervacije.txt', rezervacija_2_str)

def citanje_liste_rezervacija():
    return citanje_cuvanje.citanje_liste('rezervacije.txt', str_2_rezervacija)

def sledeci_id():
    f_rezervacije = open('rezervacije.txt', 'r')
    lines = f_rezervacije.readlines()
    f_rezervacije.close()
    
    return len(lines) + 1