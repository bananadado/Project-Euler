from math import isqrt

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x >= 5]

# Simplified, taking (mod p) where possible
# (p-5)! + (p-4)! + (p-3)! + (p-2)! + (p-1)!
# = (p-5)! * (1 + (p-4) + (p-4)(p-3) + (p-4)(p-3)(p-2) + (p-4)(p-3)(p-2)(p-1))
# take (mod p) from everything in the bracket
# = (p-5)! * 9
# = (p-1)! / ((p-1)(p-2)(p-3)(p-4)) * 9
# again
# = (p-1)! / 24 * 9

# Wilson's theorem (google ftw!!)
# = (3/8) * -1 (mod p)
# = -3/8 mod p.

# It wasn't returning the correct answer so I had to google how to do it, don't crucify me. thank you.
# I also saw that there's a way with the Extended Euclidean Algorithm that I might come back to
def S(p):
    return (p - 3) * pow(8, -1, p) % p

print(sum([S(p) for p in generatePrimes(10**8)]))
