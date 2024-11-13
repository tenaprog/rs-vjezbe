def obrni_rjecnik(rjecnik):
    obrnuti_rjecnik = {}
    for kljuc in rjecnik:
        obrnuti_rjecnik.update({rjecnik[kljuc]:kljuc})
    return obrnuti_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))