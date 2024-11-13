def ukloni_duplikate(lista):
    unikatni = []
    for i in lista:
        if i not in unikatni: 
            unikatni.append(i)
    return unikatni

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))