def registracija_korisnika(lista_korisnika, novi_korisnik):
    for korisnik in lista_korisnika:
        if korisnik['korisnicko ime'] == novi_korisnik['korisnicko ime']:
            return False
    lista_korisnika.append(novi_korisnik)

    return True

def prijava(lista_korisnika, korisnicko_ime, lozinka):
    for korisnik in lista_korisnika:
        if korisnicko_ime == korisnik['korisnicko ime'] and lozinka == korisnik['lozinka']:
            return korisnik

    return None