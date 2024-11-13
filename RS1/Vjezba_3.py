tocanBroj = 46
brojPokusaja = 0
broj_je_pogoden = False

while (broj_je_pogoden==False):
    pokusaj = int(input("Unesi broj: "))
    brojPokusaja+=1
    if(pokusaj==tocanBroj):
        broj_je_pogoden=True
        print(f"Bravo, pogodio si u {brojPokusaja} pokušaja.")
    else:
        print("Netočno!")