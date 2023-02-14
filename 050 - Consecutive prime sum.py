from itertools import count
from math import isqrt

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]

primes = generatePrimes(1000000)
chain, thePrime = 0, 0

for i in range(len(primes) - 1):
    currentTotal = primes[i]
    for j in count(1):
        currentTotal += primes[i+j]
        if currentTotal > 999999:
            break

        if j > chain and isPrime(currentTotal):
            chain = j
            thePrime = currentTotal

print(thePrime)
