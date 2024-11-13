def grupiraj_po_paritetu(lista):
    grupirani = {'parni':[], 'neparni':[]}
    for i in lista:
        if i%2==0: 
            grupirani['parni'].append(i)
        else: 
            grupirani['neparni'].append(i)
    return grupirani

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))