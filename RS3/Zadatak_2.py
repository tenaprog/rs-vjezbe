import asyncio

korisnici = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]


async def korutinaKorisnici():
    print('Dohvaćam korisnike...')
    await asyncio.sleep(3)
    print('Korisnici dohvaćeni.')
    return korisnici


async def korutinaProizvodi():
    print('Dohvaćam proizvode...')
    await asyncio.sleep(5)
    print('Proizvodi dohvaćeni.')
    return proizvodi


async def main():
    task1 = asyncio.create_task(korutinaKorisnici())
    task2 = asyncio.create_task(korutinaProizvodi())
    await asyncio.gather(task1, task2)

asyncio.run(main())
