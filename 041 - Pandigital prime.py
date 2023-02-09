from itertools import permutations
from math import isqrt

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

hi = 1
for i in range(4, 9):
    for j in permutations([str(x) for x in range(1, i)]):
        if isPrime(int("".join(j))):
            hi = int("".join(j))
print(hi)