class Proizvod:

    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, cijena: {
              self.cijena}, kolicina: {self.kolicina}")


proizvodi = [Proizvod("jabuka", 2, 546), Proizvod("kruška", 3, 457)]


def dodaj_proizvod(proizvod):
    proizvodi.append(proizvod)
