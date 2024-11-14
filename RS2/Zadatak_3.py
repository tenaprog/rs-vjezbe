# [expression for element in iterable if condition]
# [expression1 if condition else expression2 for element in iterable]
# {key_expression: value_expression for item in iterable if condition}
# {key_expression: value1 if condition else value2 for item in iterable}

import math

# Zadatak 1
parni_kvadrati = [x ** 2 for x in range(20, 51)]
print(parni_kvadrati)

# Zadatak 2
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj",
          "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(x) for x in rijeci if 'a' in x]
print(duljine_sa_slovom_a)

# Zadatak 3
kubovi = [{x: x ** 3} if x % 2 != 0 else {x: x} for x in range(1, 11)]
print(kubovi)

# Zadatak 4
korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
print(korijeni)

# Zadatak 5
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [
    {x["prezime"]: sum([x for x in x["bodovi"]])} for x in studenti]
print(zbrojeni_bodovi)
