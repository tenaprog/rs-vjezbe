from shop import proizvodi as modulProizvodi
from shop import narudzbe as modulNarudzbe


proizvodiZaDodat = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodiZaDodat:
    modulProizvodi.dodaj_proizvod(modulProizvodi.Proizvod(
        proizvod["naziv"],
        proizvod["cijena"],
        proizvod["kolicina"]
    ))

for proizvod in modulProizvodi.proizvodi:
    proizvod.ispis()


modulNarudzbe.narudzbe.append(modulNarudzbe.napravi_narudzbu(proizvodiZaDodat))
modulNarudzbe.narudzbe[0].ispis_narudzbe()
