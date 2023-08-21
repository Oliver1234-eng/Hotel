import citanje_cuvanje

def soba_2_str(soba):
    return str(soba['id']) + ',' + soba['hotel'] + ',' + str(soba['broj sobe']) + ',' + str(soba['broj kreveta']) + ',' + soba['tip'] + ',' + soba['klima'] + ',' + soba['tv'] + ',' + str(soba['cena']) + ',' + str(soba['obrisan'])

def str_2_soba(str_soba):
    podaci = str_soba.split(',')
    
    return {'id': int(podaci[0]), 'hotel': podaci[1], 'broj sobe': int(podaci[2]), 'broj kreveta': int(podaci[3]), 
    'tip': podaci[4], 'klima': podaci[5], 'tv': podaci[6], 'cena': int(podaci[7]), 'obrisan': podaci[8] == 'True'}

def cuvanje_liste_soba(lista_soba):
    citanje_cuvanje.cuvanje_liste(lista_soba, 'sobe.txt', soba_2_str)

def citanje_liste_soba():
    return citanje_cuvanje.citanje_liste('sobe.txt', str_2_soba)

def sledeci_id():
    f_sobe = open('sobe.txt', 'r')
    lines = f_sobe.readlines()
    f_sobe.close()
    
    return len(lines) + 1