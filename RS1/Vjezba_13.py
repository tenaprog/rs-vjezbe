def prvi_i_zadnji(lista):
    return (lista[0],lista[len(lista)-1])

def maks_i_min(lista):
    max = lista[0]
    min = lista[0]
    for i in lista:
        if i>max:
            max=i
        if i<min:
            min=i
    return (max,min)

def presjek(skup_1,skup_2):
    presjek= set()
    for i in skup_1:
        if i in skup_2:
            presjek.add(i)
    return presjek


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista1))

lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista2))

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))