# Not the most efficient, takes about 2 minutes to run; might come back later
from math import isqrt

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]


MAX = 10**8
MAXsqrt = isqrt(MAX) + 1
primes = set(generatePrimes(MAX))
arr = [True]*(MAX + 1)

# Essentially does the reverse operation, so we don't need to figure out the factors.
for d in range(1, MAXsqrt):
    for i in range(d, MAX//d + 1):
        if (d + i) not in primes:
            arr[d*i] = False
print(sum(x for x in range(MAX + 1) if arr[x]))
