broj = int(input("Unesi broj: "))

faktorijel = 1
for i in range(1, broj+1):
    faktorijel *=i
print(f"Faktorijel: {faktorijel}")

faktorijel = 1
while broj>0:
    faktorijel *=broj
    broj-=1
print(f"Faktorijel: {faktorijel}")