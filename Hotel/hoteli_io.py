import citanje_cuvanje

def hotel_2_str(hotel):
    return str(hotel['id']) + ',' + hotel['naziv'] + ',' + hotel['adresa'] + ',' + hotel['sobe'] + ',' + hotel['bazen'] + ',' + hotel['restoran'] + ',' + str(hotel['ocena']) + ',' + str(hotel['obrisan'])

def str_2_hotel(str_hotel):
    podaci = str_hotel.split(',')
    
    return {'id': int(podaci[0]), 'naziv': podaci[1], 'adresa': podaci[2], 'sobe': podaci[3], 'bazen': podaci[4], 
    'restoran': podaci[5], 'ocena': int(podaci[6]), 'obrisan': podaci[7] == 'True'}

def cuvanje_liste_hotela(lista_hotela):
    citanje_cuvanje.cuvanje_liste(lista_hotela, 'hoteli.txt', hotel_2_str)

def citanje_liste_hotela():
    return citanje_cuvanje.citanje_liste('hoteli.txt', str_2_hotel)

def sledeci_id():
    f_hoteli = open('hoteli.txt', 'r')
    lines = f_hoteli.readlines()
    f_hoteli.close()
    
    return len(lines) + 1