def brojanje_riječi(tekst):
    broj_rijeci = {}
    for rijec in tekst.split():
        if rijec in broj_rijeci:
            broj_rijeci[rijec]+=1
        else:    
            broj_rijeci.update({rijec:1})
    return broj_rijeci

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))