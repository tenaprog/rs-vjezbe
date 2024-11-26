import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autentifikacija(korisnik, lozinka):
    print('Provjera korisnika...')
    await asyncio.sleep(3)
    for korisnikIzBaze in baza_korisnika:
        if korisnikIzBaze['korisnicko_ime'] == korisnik['korisnicko_ime'] and korisnikIzBaze['email'] == korisnik['email']:
            return await autorizacija(korisnik, lozinka)
    return f"Korisnik {korisnik} nije pronađen."


async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    for lozinka in baza_lozinka:
        if lozinka['korisnicko_ime'] == korisnik['korisnicko_ime'] and lozinka['lozinka'] == korisnik['lozinka']:
            return f"Korisnik {korisnik}: Autorizacija uspješna."
    return f"Korisnik {korisnik}: Autorizacija neuspješna."


async def main():
    korisnik = {
        'korisnicko_ime': 'zdeslav032',
        'email': 'deso032@gmail.com',
        'lozinka': 'deso123'
    }
    rezultat = await autentifikacija(korisnik, korisnik['lozinka'])
    print(rezultat)

asyncio.run(main())
