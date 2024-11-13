def isPrime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def primes_in_range(start, end):
    prostiBrojevi = []
    for i in range(start,end):
        if isPrime(i):
            prostiBrojevi.append(i)
    return prostiBrojevi

print(isPrime(7))
print(isPrime(10)) 

print(primes_in_range(1, 10))