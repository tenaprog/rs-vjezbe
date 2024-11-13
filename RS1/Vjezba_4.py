broj = 0
while broj < 5:
    broj +=2
print(broj) 
# ispisat ce se 6

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1 
# petlja je beskonacna jer se u istoj iteraciji broj poveca pa smanji za 1, sto znaci da je stalno 0

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
# petlja je beskonacna
