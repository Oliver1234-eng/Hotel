def prijava(lista_administratora, korisnicko_ime, lozinka):
    for administrator in lista_administratora:
        if korisnicko_ime == administrator['korisnicko ime'] and lozinka == administrator['lozinka']:
            return administrator

    return None