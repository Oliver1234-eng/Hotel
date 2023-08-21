import korisnici
import korisnici_io
import recepcioneri
import recepcioneri_io
import administratori
import administratori_io
import hoteli
import hoteli_io
import ocene
import ocene_io
import rezervacije
import rezervacije_io
import sobe
import sobe_io
import izvestaji
import izvestaji_io

def pocetniMeni():
    print("\nDobrodosli u hotel\n")
    print("1 - Registracija na sistem")
    print("2 - Prijava kao korisnik")
    print("3 - Prijava kao recepcioner")
    print("4 - Prijava kao administrator")
    print("x - Kraj")

def meniKorisnika():
    print("\nUloga: korisnik\n")
    print("1 - Pregled hotela")
    print("2 - Pretraga hotela")
    print("3 - Prikaz najbolje ocenjenih hotela")
    print("4 - Kreiranje rezervacije")
    print("5 - Pregled rezervacija")
    print("6 - Ocenjivanje hotela")
    print("x - Odjava")

def pretragaHotelaKorisnik():
    print("\nPretraga hotela: \n")
    print("1 - Pretraga hotela po nazivu")
    print("2 - Pretraga hotela po adresi")
    print("3 - Pretraga hotela po oceni")
    print("4 - Kombinovana pretraga hotela")
    print("x - Nazad na glavni meni")

def meniRecepcionera():
    print("\nUloga: recepcioner\n")
    print("1 - Pretraga soba")
    print("2 - Pretraga rezervacija")
    print("3 - Izvestavanje")
    print("4 - Pregled ocena za hotele")
    print("5 - Prikaz svih soba")
    print("6 - Pregled izvestaja")
    print("x - Odjava")

def pretragaSobaRecepcioner():
    print("\nPretraga soba: \n")
    print("1 - Pretraga soba po broju sobe")
    print("2 - Pretraga soba po broju kreveta")
    print("3 - Pretraga soba po tipu(apartman/jedna soba)")
    print("4 - Pretraga soba po klimi(da/ne)")
    print("5 - Pretraga soba po tv(da/ne)")
    print("6 - Pretraga soba po ceni")
    print("7 - Kombinovana pretraga soba")
    print("x - Nazad na glavni meni")

def pretragaRezervacijaRecepcioner():
    print("\nPretraga rezervacija: \n")
    print("1 - Pretraga rezervacija po datumu kreiranja")
    print("2 - Pretraga rezervacija po datumu prijave")
    print("3 - Pretraga rezervacija po datumu odjave")
    print("4 - Pretraga rezervacija po korisniku")
    print("5 - Pretraga rezervacija po statusu(nije zapoceta/u toku/zavrsena)")
    print("6 - Kombinovana pretraga rezervacija")
    print("x - Nazad na glavni meni")

def meniAdministratora():
    print("\nUloga: administrator\n")
    print("1 - Dodavanje novih hotela")
    print("2 - Dodavanje novih recepcionera")
    print("3 - Azuriranje hotela")
    print("4 - Brisanje hotela")
    print("5 - Brisanje recepcionera")
    print("6 - Pretraga recepcionera")
    print("7 - Pregled dodatih ocena za hotele")
    print("8 - Dodavanje soba")
    print("9 - Izmena soba")
    print("x - Odjava")

def pretragaRecepcioneraAdministrator():
    print("\nPretraga recepcionera: \n")
    print("1 - Pretraga recepcionera po imenu")
    print("2 - Pretraga recepcionera po prezimenu")
    print("3 - Pretraga recepcionera po korisnickom imenu")
    print("4 - Pretraga recepcionera po email adresi")
    print("5 - Pretraga recepcionera po ulozi")
    print("6 - Pretraga recepcionera po hotelu")
    print("7 - Kombinovana pretraga recepcionera")
    print("x - Nazad na glavni meni")

def kreiranjeIzvestajaRecepcioner():
    print("\nKreiranje izvestaja")
    print("1 - Kreiraj dnevni izvestaj")
    print("2 - Kreiraj nedeljni izvestaj")
    print("3 - Kreiraj mesecni izvestaj")
    print("x - Nazad na glavni meni")

def pregledIzvestajaRecepcioner():
    print("\nPregled izvestaja")
    print("1 - Pregledaj dnevne izvestaje")
    print("2 - Pregledaj nedeljne izvestaje")
    print("3 - Pregledaj mesecne izvestaje")
    print("4 - Pregledaj sve izvestaje")
    print("x - Nazad na glavni meni")

def pregledRezervacijaKorisnik():
    print("\nPregled svojih rezervacija\n")
    print("1 - Prethodne rezervacije")
    print("2 - Rezervacije koje jos uvek nisu zapocete")
    print("3 - Rezervacije koje su u toku")

def main():
    while True:
        pocetniMeni()
        izbor = input("Opcija: ")
        if izbor == '1':
            korisnicko_ime = input("Korisnicko ime: ")
            lozinka = input("Lozinka: ")
            ime = input("Ime: ")
            prezime = input("Prezime: ")
            telefon = input("Kontakt telefon: ")
            email = input("Email adresa: ")
            uloga = "korisnik"
            novi_korisnik = {'id': korisnici_io.sledeci_id(), 'korisnicko ime': korisnicko_ime, 'lozinka': lozinka, 'ime': ime, 
            'prezime': prezime, 'telefon': telefon, 'email': email, 'uloga': uloga, 'obrisan': False}
            lista_korisnika = korisnici_io.citanje_liste_korisnika()
            korisnici.registracija_korisnika(lista_korisnika, novi_korisnik)
            korisnici_io.cuvanje_liste_korisnika(lista_korisnika)
            print("\nUspesna registracija\n")
        elif izbor == '2':
            lista_korisnika = korisnici_io.citanje_liste_korisnika()
            korisnicko_ime = input("Korisnicko ime: ")
            lozinka = input("Lozinka: ")
            korisnik = korisnici.prijava(lista_korisnika, korisnicko_ime, lozinka)
            while not korisnik:
                print("\nUneti podaci nisu validni! Pokusajte ponovo")
                korisnicko_ime = input("Korisnicko ime: ")
                lozinka = input("Lozinka: ")
                korisnik = korisnici.prijava(lista_korisnika, korisnicko_ime, lozinka)
            while True:
                meniKorisnika()
                izbor = input("Opcija: ")
                if izbor == '1':
                    lista_hotela = hoteli_io.citanje_liste_hotela()
                    lista_hotela = hoteli.sortiranje_liste_hotela(lista_hotela)
                    hoteli.zaglavlje()
                    hoteli.prikaz_svih_hotela(lista_hotela)
                elif izbor == '2':
                    while True:
                        pretragaHotelaKorisnik()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            naziv = input("Naziv: ")
                            lista_hotela = hoteli_io.citanje_liste_hotela()
                            lista_hotela = hoteli.pronalazenje_po_nazivu(lista_hotela, naziv)
                            hoteli.zaglavlje()
                            hoteli.prikaz_svih_hotela(lista_hotela)
                        elif izbor == '2':
                            adresa = input("Adresa: ")
                            lista_hotela = hoteli_io.citanje_liste_hotela()
                            lista_hotela = hoteli.pronalazenje_po_adresi(lista_hotela, adresa)
                            hoteli.zaglavlje()
                            hoteli.prikaz_svih_hotela(lista_hotela)
                        elif izbor == '3':
                            ocena = input("Ocena: ")
                            lista_hotela = hoteli_io.citanje_liste_hotela()
                            lista_hotela = hoteli.pronalazenje_po_oceni(lista_hotela, ocena)
                            hoteli.zaglavlje()
                            hoteli.prikaz_svih_hotela(lista_hotela)
                        elif izbor == '4':
                            naziv = input("Naziv: ")
                            adresa = input("Adresa: ")
                            ocena = input("Ocena: ")
                            lista_hotela = hoteli_io.citanje_liste_hotela()
                            lista_hotela = hoteli.kombinovana_pretraga(lista_hotela, naziv, adresa, ocena)
                            hoteli.zaglavlje()
                            hoteli.prikaz_svih_hotela(lista_hotela)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '3':
                    lista_hotela = hoteli_io.citanje_liste_hotela()
                    lista_hotela = hoteli.sortiranje_liste_hotela(lista_hotela)
                    hoteli.zaglavlje()
                    hoteli.prikaz_najboljih_hotela(lista_hotela)
                elif izbor == '4':
                    hotel = input("Naziv hotela: ")
                    while not (hotel == 'Air Hotel' or hotel == 'Hotel de Glace' or hotel == 'Ledeni Hotel' or hotel == 'Hotel Jade Screen' or hotel == 'Magic Mountain Lodge'):
                        print("\nHotel sa takvim nazivom ne postoji!")
                        hotel = input("Naziv hotela: ")
                    sobe = input("Sobe za rezervisanje(format soba1_soba2_soba3, na primer 1_2_3): ")
                    dan_kreiranja = input("Dan kreiranja rezervacije(1-31): ")
                    while not (dan_kreiranja == '1' or dan_kreiranja == '2' or dan_kreiranja == '3' or dan_kreiranja == '4' or dan_kreiranja == '5' or dan_kreiranja == '6' or dan_kreiranja == '7' or dan_kreiranja == '8' or dan_kreiranja == '9' or dan_kreiranja == '10' or dan_kreiranja == '11' or dan_kreiranja == '12' or dan_kreiranja == '13' or dan_kreiranja == '14' or dan_kreiranja == '15' or dan_kreiranja == '16' or dan_kreiranja == '17' or dan_kreiranja == '18' or dan_kreiranja == '19' or dan_kreiranja == '20' or dan_kreiranja == '21' or dan_kreiranja == '22' or dan_kreiranja == '23' or dan_kreiranja == '24' or dan_kreiranja == '25' or dan_kreiranja == '26' or dan_kreiranja == '27' or dan_kreiranja == '28' or dan_kreiranja == '29' or dan_kreiranja == '30' or dan_kreiranja == '31'):
                        print("\nUnesite validan dan!")
                        dan_kreiranja = input("Dan kreiranja rezervacije(1-31): ")
                    mesec_kreiranja = input("Mesec kreiranje rezervacije(1-12): ")
                    while not (mesec_kreiranja == '1' or mesec_kreiranja == '2' or mesec_kreiranja == '3' or mesec_kreiranja == '4' or mesec_kreiranja == '5' or mesec_kreiranja == '6' or mesec_kreiranja == '7' or mesec_kreiranja == '8' or mesec_kreiranja == '9' or mesec_kreiranja == '10' or mesec_kreiranja == '11' or mesec_kreiranja == '12'):
                        print("\nUnesite validan mesec!")
                        mesec_kreiranja = input("Mesec kreiranje rezervacije(1-12): ")
                    godina_kreiranja = input("Godina kreiranja rezervacije(2022): ")
                    while not (godina_kreiranja == '2022'):
                        print("\nUnesite validnu godinu!")
                        godina_kreiranja = input("Godina kreiranja rezervacije(2022): ")
                    dan_prijave = input("Dan prijave u hotel(1-31): ")
                    while not (dan_prijave == '1' or dan_prijave == '2' or dan_prijave == '3' or dan_prijave == '4' or dan_prijave == '5' or dan_prijave == '6' or dan_prijave == '7' or dan_prijave == '8' or dan_prijave == '9' or dan_prijave == '10' or dan_prijave == '11' or dan_prijave == '12' or dan_prijave == '13' or dan_prijave == '14' or dan_prijave == '15' or dan_prijave == '16' or dan_prijave == '17' or dan_prijave == '18' or dan_prijave == '19' or dan_prijave == '20' or dan_prijave == '21' or dan_prijave == '22' or dan_prijave == '23' or dan_prijave == '24' or dan_prijave == '25' or dan_prijave == '26' or dan_prijave == '27' or dan_prijave == '28' or dan_prijave == '29' or dan_prijave == '30' or dan_prijave == '31'):
                        print("\nUnesite validan dan!")
                        dan_prijave = input("Dan prijave u hotel(1-31): ")
                    mesec_prijave = input("Mesec prijave u hotel(1-12): ")
                    while not (mesec_prijave == '1' or mesec_prijave == '2' or mesec_prijave == '3' or mesec_prijave == '4' or mesec_prijave == '5' or mesec_prijave == '6' or mesec_prijave == '7' or mesec_prijave == '8' or mesec_prijave == '9' or mesec_prijave == '10' or mesec_prijave == '11' or mesec_prijave == '12'):
                        print("\nUnesite validan mesec!")
                        mesec_prijave = input("Mesec prijave u hotel(1-12): ")
                    godina_prijave = input("Godina prijave u hotel(2022): ")
                    while not (godina_prijave == '2022'):
                        print("\nUnesite validnu godinu!")
                        godina_prijave = input("Godina prijave u hotel(2022): ")
                    dan_odjave = input("Dan odjave iz hotela(1-31): ")
                    while not (dan_odjave == '1' or dan_odjave == '2' or dan_odjave == '3' or dan_odjave == '4' or dan_odjave == '5' or dan_odjave == '6' or dan_odjave == '7' or dan_odjave == '8' or dan_odjave == '9' or dan_odjave == '10' or dan_odjave == '11' or dan_odjave == '12' or dan_odjave == '13' or dan_odjave == '14' or dan_odjave == '15' or dan_odjave == '16' or dan_odjave == '17' or dan_odjave == '18' or dan_odjave == '19' or dan_odjave == '20' or dan_odjave == '21' or dan_odjave == '22' or dan_odjave == '23' or dan_odjave == '24' or dan_odjave == '25' or dan_odjave == '26' or dan_odjave == '27' or dan_odjave == '28' or dan_odjave == '29' or dan_odjave == '30' or dan_odjave == '31'):
                        print("\nUnesite validan dan!")
                        dan_odjave = input("Dan odjave iz hotela(1-31): ")
                    mesec_odjave = input("Mesec odjave iz hotela(1-12): ")
                    while not (mesec_odjave == '1' or mesec_odjave == '2' or mesec_odjave == '3' or mesec_odjave == '4' or mesec_odjave == '5' or mesec_odjave == '6' or mesec_odjave == '7' or mesec_odjave == '8' or mesec_odjave == '9' or mesec_odjave == '10' or mesec_odjave == '11' or mesec_odjave == '12'):
                        print("\nUnesite validan mesec!")
                        mesec_odjave = input("Mesec odjave iz hotela(1-12): ")
                    godina_odjave = input("Godina odjave iz hotela(2022): ")
                    while not (godina_odjave == '2022'):
                        print("\nUnesite validnu godinu!")
                        godina_prijave = input("Godina odjave iz hotela(2022): ")
                    korisnik = input("Vase korisnicko ime: ")
                    while not (korisnik == 'pera' or korisnik == 'mika'):
                        print("\nKorisnik sa tim korisnickim imenom ne postoji u sistemu!")
                        korisnik = input("Vase korisnicko ime: ")
                    status = "nije zapoceta"
                    nova_rezervacija = {'id': rezervacije_io.sledeci_id(), 'hotel': hotel, 'sobe': sobe, 'dan kreiranja': dan_kreiranja, 
                    'mesec kreiranja': mesec_kreiranja, 'godina kreiranja': godina_kreiranja, 'dan prijave': dan_prijave, 'mesec prijave': mesec_prijave, 
                    'godina prijave': godina_prijave, 'dan odjave': dan_odjave, 'mesec odjave': mesec_odjave, 'godina odjave': godina_odjave, 
                    'korisnik': korisnik, 'status': status, 'obrisan': False}
                    lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                    rezervacije.dodavanje_nove_rezervacije(lista_rezervacija, nova_rezervacija)
                    rezervacije_io.cuvanje_liste_rezervacija(lista_rezervacija)
                    print("\nUspesno dodata rezervacija\n")
                elif izbor == '5':
                    while True:
                        pregledRezervacijaKorisnik()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.sortiranje_liste_rezervacija(lista_rezervacija)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_zavrsenih_rezervacija(lista_rezervacija)
                        elif izbor == '2':
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.sortiranje_liste_rezervacija(lista_rezervacija)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_nezapocetih_rezervacija(lista_rezervacija)
                        elif izbor == '3':
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.sortiranje_liste_rezervacija(lista_rezervacija)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_u_toku_rezervacija(lista_rezervacija)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '6':
                    naziv = input("Naziv hotela: ")
                    while not (naziv == 'Air Hotel' or naziv == 'Hotel de Glace' or naziv == 'Ledeni Hotel' or naziv == 'Hotel Jade Screen' or naziv == 'Magic Mountain Lodge'):
                        print("\nHotel sa takvim nazivom ne postoji!")
                        naziv = input("Naziv hotela: ")
                    ocena = input("Ocena: ")
                    while not (ocena == '1' or ocena == '2' or ocena == '3' or ocena == '4' or ocena == '5'):
                        print("\nHotel se moze oceniti ocenom 1 do 5")
                        ocena = input("Ocena: ")
                    nova_ocena = {'id': ocene_io.sledeci_id(), 'naziv': naziv, 'ocena': ocena, 'obrisan': False}
                    lista_ocena = ocene_io.citanje_liste_ocena()
                    ocene.dodavanje_nove_ocene(lista_ocena, nova_ocena)
                    ocene_io.cuvanje_liste_ocena(lista_ocena)
                    print("\nUspesno dodata ocena\n")
                elif izbor == 'x':
                    print("Dovidjenja\n")
                    break
                else:
                    print("Nepoznata komanda")
        elif izbor == '3':
            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
            korisnicko_ime = input("Korisnicko ime: ")
            lozinka = input("Lozinka: ")
            recepcioner = recepcioneri.prijava(lista_recepcionera, korisnicko_ime, lozinka)
            while not recepcioner:
                print("\nUneti podaci nisu validni! Pokusajte ponovo")
                korisnicko_ime = input("Korisnicko ime: ")
                lozinka = input("Lozinka: ")
                recepcioner = recepcioneri.prijava(lista_recepcionera, korisnicko_ime, lozinka)
            while True:
                meniRecepcionera()
                izbor = input("Opcija: ")
                if izbor == '1':
                    while True:
                        pretragaSobaRecepcioner()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            broj_sobe = input("Broj sobe: ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_broju_sobe(lista_soba, broj_sobe)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '2':
                            broj_kreveta = input("Broj kreveta: ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_broju_kreveta(lista_soba, broj_kreveta)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '3':
                            tip = input("Tip sobe(apartman/jedna soba): ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_tipu(lista_soba, tip)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '4':
                            klima = input("Klima(da/ne): ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_klimi(lista_soba, klima)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '5':
                            tv = input("TV(da/ne): ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_tvu(lista_soba, tv)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '6':
                            cena = input("Cena: ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.pronalazenje_po_ceni(lista_soba, cena)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == '7':
                            broj_sobe = input("Broj sobe: ")
                            broj_kreveta = input("Broj kreveta: ")
                            tip = input("Tip sobe(apartman/jedna soba): ")
                            klima = input("Klima(da/ne): ")
                            tv = input("TV(da/ne): ")
                            cena = input("Cena: ")
                            lista_soba = sobe_io.citanje_liste_soba()
                            lista_soba = ocene.kombinovana_pretraga(lista_soba, broj_sobe, broj_kreveta, tip, klima, tv, cena)
                            ocene.zaglavlje_sobe()
                            ocene.prikaz_svih_soba(lista_soba)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '2':
                    while True:
                        pretragaRezervacijaRecepcioner()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            dan_kreiranja = input("Dan kreiranja: ")
                            mesec_kreiranja = input("Mesec kreiranja: ")
                            godina_kreiranja = input("Godina kreiranja: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.kombinovana_pretraga_po_datumu_kreiranja(lista_rezervacija, dan_kreiranja, mesec_kreiranja, godina_kreiranja)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == '2':
                            dan_prijave = input("Dan prijave: ")
                            mesec_prijave = input("Mesec prijave: ")
                            godina_prijave = input("Godina prijave: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.kombinovana_pretraga_po_datumu_prijave(lista_rezervacija, dan_prijave, mesec_prijave, godina_prijave)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == '3':
                            dan_odjave = input("Dan odjave: ")
                            mesec_odjave = input("Mesec odjave: ")
                            godina_odjave = input("Godina odjave: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.kombinovana_pretraga_po_datumu_odjave(lista_rezervacija, dan_odjave, mesec_odjave, godina_odjave)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == '4':
                            korisnik = input("Korisnicko ime korisnika: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.pronalazenje_po_korisniku(lista_rezervacija, korisnik)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == '5':
                            status = input("Status rezervacije: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.pronalazenje_po_statusu(lista_rezervacija, status)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == '6':
                            dan_kreiranja = input("Dan kreiranja: ")
                            mesec_kreiranja = input("Mesec kreiranja: ")
                            godina_kreiranja = input("Godina kreiranja: ")
                            dan_prijave = input("Dan prijave: ")
                            mesec_prijave = input("Mesec prijave: ")
                            godina_prijave = input("Godina prijave: ")
                            dan_odjave = input("Dan odjave: ")
                            mesec_odjave = input("Mesec odjave: ")
                            godina_odjave = input("Godina odjave: ")
                            korisnik = input("Korisnicko ime korisnika: ")
                            status = input("Status rezervacije: ")
                            lista_rezervacija = rezervacije_io.citanje_liste_rezervacija()
                            lista_rezervacija = rezervacije.kombinovana_pretraga(lista_rezervacija, dan_kreiranja, mesec_kreiranja, godina_kreiranja, dan_prijave, mesec_prijave, godina_prijave, dan_odjave, mesec_odjave, godina_odjave, korisnik, status)
                            rezervacije.zaglavlje()
                            rezervacije.prikaz_svih_rezervacija(lista_rezervacija)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '3':
                    while True:
                        kreiranjeIzvestajaRecepcioner()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            realizovane_rezervacije = input("Ukupan broj realizovanih rezervacija: ")
                            izdate_sobe = input("Ukupan broj izdatih soba: ")
                            ukupna_zarada = input("Ukupna zarada za taj period: ")
                            prosecna_ocena = input("Prosecna ocena za taj period: ")
                            vrsta = "dnevni"
                            novi_izvestaj = {'id': izvestaji_io.sledeci_id(), 'realizovane rezervacije': realizovane_rezervacije, 'izdate sobe': izdate_sobe,
                            'ukupna zarada': ukupna_zarada, 'prosecna ocena': prosecna_ocena, 'vrsta': vrsta, 'obrisan': False}
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.dodavanje_dnevnog_izvestaja(lista_izvestaja, novi_izvestaj)
                            izvestaji_io.cuvanje_liste_izvestaja(lista_izvestaja)
                            print("\nUspesno dodat dnevni izvestaj\n")
                        elif izbor == '2':
                            realizovane_rezervacije = input("Ukupan broj realizovanih rezervacija: ")
                            izdate_sobe = input("Ukupan broj izdatih soba: ")
                            ukupna_zarada = input("Ukupna zarada za taj period: ")
                            prosecna_ocena = input("Prosecna ocena za taj period: ")
                            vrsta = "nedeljni"
                            novi_izvestaj = {'id': izvestaji_io.sledeci_id(), 'realizovane rezervacije': realizovane_rezervacije, 'izdate sobe': izdate_sobe,
                            'ukupna zarada': ukupna_zarada, 'prosecna ocena': prosecna_ocena, 'vrsta': vrsta, 'obrisan': False}
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.dodavanje_nedeljnog_izvestaja(lista_izvestaja, novi_izvestaj)
                            izvestaji_io.cuvanje_liste_izvestaja(lista_izvestaja)
                            print("\nUspesno dodat nedeljni izvestaj\n")
                        elif izbor == '3':
                            realizovane_rezervacije = input("Ukupan broj realizovanih rezervacija: ")
                            izdate_sobe = input("Ukupan broj izdatih soba: ")
                            ukupna_zarada = input("Ukupna zarada za taj period: ")
                            prosecna_ocena = input("Prosecna ocena za taj period: ")
                            vrsta = "mesecni"
                            novi_izvestaj = {'id': izvestaji_io.sledeci_id(), 'realizovane rezervacije': realizovane_rezervacije, 'izdate sobe': izdate_sobe,
                            'ukupna zarada': ukupna_zarada, 'prosecna ocena': prosecna_ocena, 'vrsta': vrsta, 'obrisan': False}
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.dodavanje_mesecnog_izvestaja(lista_izvestaja, novi_izvestaj)
                            izvestaji_io.cuvanje_liste_izvestaja(lista_izvestaja)
                            print("\nUspesno mesecni izvestaj\n")
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '4':
                    lista_ocena = ocene_io.citanje_liste_ocena()
                    lista_ocena = ocene.sortiranje_liste_ocena(lista_ocena)
                    ocene.zaglavlje()
                    ocene.prikaz_svih_ocena(lista_ocena)
                elif izbor == '5':
                    lista_soba = sobe_io.citanje_liste_soba()
                    lista_soba = ocene.sortiranje_liste_soba(lista_soba)
                    ocene.zaglavlje_sobe()
                    ocene.prikaz_svih_soba(lista_soba)
                elif izbor == '6':
                    while True:
                        pregledIzvestajaRecepcioner()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.zaglavlje()
                            izvestaji.prikaz_dnevnih_izvestaja(lista_izvestaja)
                        elif izbor == '2':
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.zaglavlje()
                            izvestaji.prikaz_nedeljnih_izvestaja(lista_izvestaja)
                        elif izbor == '3':
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.zaglavlje()
                            izvestaji.prikaz_mesecnih_izvestaja(lista_izvestaja)
                        elif izbor == '4':
                            lista_izvestaja = izvestaji_io.citanje_liste_izvestaja()
                            izvestaji.zaglavlje()
                            izvestaji.prikaz_svih_izvestaja(lista_izvestaja)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == 'x':
                    print("Dovidjenja\n")
                    break
                else:
                    print("Nepoznata komanda")
        elif izbor == '4':
            lista_administratora = administratori_io.citanje_liste_administratora()
            korisnicko_ime = input("Korisnicko ime: ")
            lozinka = input("Lozinka: ")
            administrator = administratori.prijava(lista_administratora, korisnicko_ime, lozinka)
            while not administrator:
                print("\nUneti podaci nisu validni! Pokusajte ponovo")
                korisnicko_ime = input("Korisnicko ime: ")
                lozinka = input("Lozinka: ")
                administrator = administratori.prijava(lista_administratora, korisnicko_ime, lozinka)
            while True:
                meniAdministratora()
                izbor = input("Opcija: ")
                if izbor == '1':
                    naziv = input("Naziv: ")
                    adresa = input("Adresa: ")
                    sobe = input("Sobe(format soba1_soba2_soba3, na primer 1_2_3): ")
                    bazen = input("Bazen(da/ne): ")
                    while not (bazen == 'da' or bazen == 'ne'):
                        bazen = input("Bazen(da/ne): ")
                    restoran = input("Restoran(da/ne): ")
                    while not (restoran == 'da' or restoran == 'ne'):
                        restoran = input("Restoran(da/ne): ")
                    ocena = 5
                    novi_hotel = {'id': hoteli_io.sledeci_id(), 'naziv': naziv, 'adresa': adresa, 'sobe': sobe, 
                    'bazen': bazen, 'restoran': restoran, 'ocena': ocena, 'obrisan': False}
                    lista_hotela = hoteli_io.citanje_liste_hotela()
                    hoteli.dodavanje_novog_hotela(lista_hotela, novi_hotel)
                    hoteli_io.cuvanje_liste_hotela(lista_hotela)
                    print("\nUspesno dodat hotel\n")
                elif izbor == '2':
                    korisnicko_ime = input("Korisnicko ime: ")
                    lozinka = input("Lozinka: ")
                    ime = input("Ime: ")
                    prezime = input("Prezime: ")
                    telefon = input("Kontakt telefon: ")
                    email = input("Email adresa: ")
                    uloga = "recepcioner"
                    hotel = input("Sifra hotela: ")
                    while not (hotel == '1' or hotel == '2' or hotel == '3' or hotel == '4' or hotel == '5'):
                        print("\nHotel sa tom sifrom ne postoji!")
                        hotel = input("Sifra hotela: ")
                    novi_recepcioner = {'id': recepcioneri_io.sledeci_id(), 'korisnicko ime': korisnicko_ime, 'lozinka': lozinka, 'ime': ime, 
                    'prezime': prezime, 'telefon': telefon, 'email': email, 'uloga': uloga, 'obrisan': False, 'hotel': hotel}
                    lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                    recepcioneri.dodavanje_novog_recepcionera(lista_recepcionera, novi_recepcioner)
                    recepcioneri_io.cuvanje_liste_recepcionera(lista_recepcionera)
                    print("\nUspesno dodat recepcioner\n")
                elif izbor == '3':
                    naziv = input("Naziv: ")
                    lista_hotela = hoteli_io.citanje_liste_hotela()
                    sobe = input("Sobe(format soba1_soba2_soba3, na primer 1_2_3): ")
                    bazen = input("Bazen(da/ne): ")
                    while not (bazen == 'da' or bazen == 'ne'):
                        bazen = input("Bazen(da/ne): ")
                    restoran = input("Restoran(da/ne): ")
                    while not (restoran == 'da' or restoran == 'ne'):
                        restoran = input("Restoran(da/ne): ")
                    hoteli.izmena_podataka_o_hotelu(lista_hotela, naziv, sobe, bazen, restoran)
                    hoteli_io.cuvanje_liste_hotela(lista_hotela)
                    print("\nHotel uspesno izmenjen \n")
                elif izbor == '4':
                    naziv = input("Naziv: ")
                    lista_hotela = hoteli_io.citanje_liste_hotela()
                    hoteli.brisanje_hotela(lista_hotela, naziv)
                    hoteli_io.cuvanje_liste_hotela(lista_hotela)
                elif izbor == '5':
                    korisnicko_ime = input("Korisnicko ime: ")
                    lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                    recepcioneri.brisanje_recepcionera(lista_recepcionera, korisnicko_ime)
                    recepcioneri_io.cuvanje_liste_recepcionera(lista_recepcionera)
                elif izbor == '6':
                    while True:
                        pretragaRecepcioneraAdministrator()
                        izbor = input("Opcija: ")
                        if izbor == '1':
                            ime = input("Ime: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_imenu(lista_recepcionera, ime)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '2':
                            prezime = input("Prezime: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_prezimenu(lista_recepcionera, prezime)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '3':
                            korisnicko_ime = input("Korisnicko ime: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_korisnickom_imenu(lista_recepcionera, korisnicko_ime)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '4':
                            email = input("Email adresa: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_emailu(lista_recepcionera, email)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '5':
                            uloga = input("Uloga(recepcioner): ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_ulozi(lista_recepcionera, uloga)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '6':
                            hotel = input("ID hotela u kom je zaposlen: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.pronalazenje_po_hotelu(lista_recepcionera, hotel)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == '7':
                            ime = input("Ime: ")
                            prezime = input("Prezime: ")
                            korisnicko_ime = input("Korisnicko ime: ")
                            email = input("Email adresa: ")
                            uloga = input("Uloga(recepcioner): ")
                            hotel = input("ID hotela u kom je zaposlen: ")
                            lista_recepcionera = recepcioneri_io.citanje_liste_recepcionera()
                            lista_recepcionera = recepcioneri.kombinovana_pretraga(lista_recepcionera, ime, prezime, korisnicko_ime, email, uloga, hotel)
                            recepcioneri.zaglavlje()
                            recepcioneri.prikaz_svih_recepcionera(lista_recepcionera)
                        elif izbor == 'x':
                            break
                        else:
                            print("Nepoznata komanda")
                elif izbor == '7':
                    lista_ocena = ocene_io.citanje_liste_ocena()
                    lista_ocena = ocene.sortiranje_liste_ocena(lista_ocena)
                    ocene.zaglavlje()
                    ocene.prikaz_svih_ocena(lista_ocena)
                elif izbor == '8':
                    hotel = input("Naziv hotela: ")
                    while not (hotel == 'Air Hotel' or hotel == 'Hotel de Glace' or hotel == 'Ledeni Hotel' or hotel == 'Hotel Jade Screen' or hotel == 'Magic Mountain Lodge'):
                        print("\nHotel sa takvim nazivom ne postoji!")
                        hotel = input("Naziv hotela: ")
                    broj_sobe = input("Broj sobe: ")
                    broj_kreveta = input("Broj kreveta: ")
                    tip = input("Tip sobe(apartman/jedna soba): ")
                    while not (tip == 'apartman' or tip == 'jedna soba'):
                        print("\nNe postoji takav tip sobe")
                        tip = input("Tip sobe(apartman/jedna soba): ")
                    klima = input("Klima(da/ne): ")
                    while not (klima == 'da' or klima == 'ne'):
                        print("\nGreska prilikom unosa")
                        klima = input("Klima(da/ne): ")
                    tv = input("TV(da/ne): ")
                    while not (tv == 'da' or tv == 'ne'):
                        print("\nGreska prilikom unosa")
                        tv = input("TV(da/ne): ")
                    cena = input("Cena: ")
                    nova_soba = {'id': sobe_io.sledeci_id(), 'hotel': hotel, 'broj sobe': broj_sobe, 'broj kreveta': broj_kreveta, 
                    'tip': tip, 'klima': klima, 'tv': tv, 'cena': cena, 'obrisan': False}
                    lista_soba = sobe_io.citanje_liste_soba()
                    ocene.dodavanje_nove_sobe(lista_soba, nova_soba)
                    sobe_io.cuvanje_liste_soba(lista_soba)
                    print("\nUspesno dodata soba\n")
                elif izbor == '9':
                    broj_sobe = input("Broj sobe: ")
                    lista_soba = sobe_io.citanje_liste_soba()
                    tip = input("Tip sobe(apartman/jedna soba): ")
                    while not (tip == 'apartman' or tip == 'jedna soba'):
                        print("\nNe postoji takav tip sobe")
                        tip = input("Tip sobe(apartman/jedna soba): ")
                    klima = input("Klima(da/ne): ")
                    while not (klima == 'da' or klima == 'ne'):
                        print("\nGreska prilikom unosa")
                        klima = input("Klima(da/ne): ")
                    tv = input("TV(da/ne): ")
                    while not (tv == 'da' or tv == 'ne'):
                        print("\nGreska prilikom unosa")
                        tv = input("TV(da/ne): ")
                    ocene.izmena_podataka_o_sobi(lista_soba, broj_sobe, tip, klima, tv)
                    sobe_io.cuvanje_liste_soba(lista_soba)
                    print("\nSoba uspesno izmenjena \n")
                elif izbor == 'x':
                    print("Dovidjenja\n")
                    break
                else:
                    print("Nepoznata komanda")
        elif izbor == 'x':
            print("Dovidjenja")
            break
        else:
            print("Nepoznata komanda")

if __name__ == '__main__':
    main()