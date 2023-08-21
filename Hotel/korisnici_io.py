import citanje_cuvanje

def korisnik_2_str(korisnik):
    return str(korisnik['id']) + ',' + korisnik['korisnicko ime'] + ',' + korisnik['lozinka'] + ',' + korisnik['ime'] + ',' + korisnik['prezime'] + ',' + korisnik['telefon'] + ',' + korisnik['email'] + ',' + korisnik['uloga'] + ',' + str(korisnik['obrisan'])

def str_2_korisnik(str_korisnik):
    podaci = str_korisnik.split(',')
    
    return {'id': int(podaci[0]), 'korisnicko ime': podaci[1], 'lozinka': podaci[2], 'ime': podaci[3], 
    'prezime': podaci[4], 'telefon': podaci[5], 'email': podaci[6], 'uloga': podaci[7], 
    'obrisan': podaci[8] == 'True'}

def cuvanje_liste_korisnika(lista_korisnika):
    citanje_cuvanje.cuvanje_liste(lista_korisnika, 'korisnici.txt', korisnik_2_str)

def citanje_liste_korisnika():
    return citanje_cuvanje.citanje_liste('korisnici.txt', str_2_korisnik)

def sledeci_id():
    f_korisnici = open('korisnici.txt', 'r')
    lines = f_korisnici.readlines()
    f_korisnici.close()
    
    return len(lines) + 1