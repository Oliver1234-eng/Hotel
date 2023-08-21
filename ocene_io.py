import citanje_cuvanje

def ocena_2_str(ocena):
    return str(ocena['id']) + ',' + ocena['naziv'] + ',' + str(ocena['ocena']) + ',' + str(ocena['obrisan'])

def str_2_ocena(str_ocena):
    podaci = str_ocena.split(',')
    
    return {'id': int(podaci[0]), 'naziv': podaci[1], 'ocena': int(podaci[2]), 'obrisan': podaci[3] == 'True'}

def cuvanje_liste_ocena(lista_ocena):
    citanje_cuvanje.cuvanje_liste(lista_ocena, 'ocene.txt', ocena_2_str)

def citanje_liste_ocena():
    return citanje_cuvanje.citanje_liste('ocene.txt', str_2_ocena)

def sledeci_id():
    f_ocene = open('ocene.txt', 'r')
    lines = f_ocene.readlines()
    f_ocene.close()
    
    return len(lines) + 1