import citanje_cuvanje

def izvestaj_2_str(izvestaj):
    return str(izvestaj['id']) + ',' + str(izvestaj['realizovane rezervacije']) + ',' + str(izvestaj['izdate sobe']) + ',' + str(izvestaj['ukupna zarada']) + ',' + str(izvestaj['prosecna ocena']) + ',' + izvestaj['vrsta'] + ',' + str(izvestaj['obrisan'])

def str_2_izvestaj(str_izvestaj):
    podaci = str_izvestaj.split(',')
    
    return {'id': int(podaci[0]), 'realizovane rezervacije': int(podaci[1]), 'izdate sobe': int(podaci[2]), 
    'ukupna zarada': int(podaci[3]), 'prosecna ocena': int(podaci[4]), 'vrsta': podaci[5], 'obrisan': podaci[6] == 'True'}

def cuvanje_liste_izvestaja(lista_izvestaja):
    citanje_cuvanje.cuvanje_liste(lista_izvestaja, 'izvestaji.txt', izvestaj_2_str)

def citanje_liste_izvestaja():
    return citanje_cuvanje.citanje_liste('izvestaji.txt', str_2_izvestaj)

def sledeci_id():
    f_izvestaji = open('izvestaji.txt', 'r')
    lines = f_izvestaji.readlines()
    f_izvestaji.close()
    
    return len(lines) + 1