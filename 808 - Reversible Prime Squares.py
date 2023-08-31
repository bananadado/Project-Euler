# Easily brute force in under 15s
from math import isqrt

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]


total = set()
count = 0
primes = generatePrimes(10 ** 8)
primeSquare = [x ** 2 for x in primes]
primeSet = set(primeSquare)

for i in primeSquare:
    if int(str(i)[::-1]) != i and (int(str(i)[::-1]) in primeSet):
        total.add(i)
        total.add(int(str(i)[::-1]))
    if len(total) >= 50:
        print(sum(total))
        quit()
