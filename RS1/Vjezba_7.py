def postoji_znak(lozinka):
    return any(i.isdigit() for i in lozinka)

def postoji_rijec(rijec, lozinka):
    return rijec.lower() in lozinka.lower()

def provjera_lozinke(lozinka):
    if len(lozinka) not in range(8,15):
        return "Lozinka mora sadržavati između 8 i 15 znakova."    
    if lozinka==lozinka.lower() or postoji_znak(lozinka)==False:
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."
    if postoji_rijec("password",lozinka) or postoji_rijec("lozinka",lozinka):
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'."
    return "Lozinka je jaka!"
    

lozinka = input("Unesi lozinku: ")
print(provjera_lozinke(lozinka))