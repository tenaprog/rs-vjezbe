class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_opis = [f"{proizvod['naziv']} x {
            proizvod['kolicina']}" for proizvod in self.proizvodi]
        print(f"Naručeni proizvodi: {', '.join(proizvodi_opis)}, Ukupna cijena: {
              self.ukupna_cijena} EUR")


def napravi_narudzbu(proizvodi):
    if not isinstance(proizvodi, list):
        return print("Nije lista")
    if len(proizvodi) < 1:
        return print("Prazna lista")
    for proizvod in proizvodi:
        if not isinstance(proizvod, dict):
            return print("Nije rijecnik")
        if {"naziv", "cijena", "kolicina"}.issubset(proizvod):
            return print("Nema kljuceve")
        if (proizvod["kolicina"] < 1):
            return print(f"Proizvod {proizvod.naziv} nije dostupan!")

    ukupna_cijena = sum(
        proizvod["cijena"] * proizvod["kolicina"] for proizvod in proizvodi)
    return Narudzba(proizvodi, ukupna_cijena)


narudzbe = []
