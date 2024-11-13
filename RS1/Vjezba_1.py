prviBroj = float(input("Unesi prvi broj: "))
drugiBroj = float(input("Unesi drugi broj: "))
operator = input("Unesi operator: ")

def izracunajRezultat(prviBroj, drugiBroj, operator):
    if operator == "+":
        return prviBroj + drugiBroj
    if operator == "-":
        return prviBroj - drugiBroj
    if operator == "*":
        return prviBroj * drugiBroj
    if operator == "/":
        return prviBroj / drugiBroj

if drugiBroj == "0" and operator == "/":
    print("Dijeljenje s nulom nije dozvoljeno!")
elif operator in ["+", "-", "*", "/"]:
    print(f"Rezultat operacije {prviBroj} {operator} {drugiBroj} je {izracunajRezultat(prviBroj, drugiBroj, operator)}")
else:
    print("Nepodržani operator!")