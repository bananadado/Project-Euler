from math import isqrt

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i ** 2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]


def isPrime(n):
    if n in primeLookup:
        return True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def combo(l):
    for x in [[int(str(l[x]) + str(l[-1])), int(str(l[-1]) + str(l[x]))] for x in range(len(l)-1)]:
        if not isPrime(x[0]) or not isPrime(x[1]):
            return False
    return True


def chaininator(chain):
    if len(chain) == 5:
        return chain
    for p in primes[primes.index(chain[-1]) + 1 if len(chain) > 1 else 0:]:
        if combo(chain + [p]):
            nextChain = chaininator(chain + [p])
            if len(nextChain) == 5:
                return nextChain
    return chain

primes = generatePrimes(10000)
primeLookup = set(primes)
chain = []
while len(chain) != 5:
    chain = chaininator([primes.pop(0)])
print(sum(chain))
