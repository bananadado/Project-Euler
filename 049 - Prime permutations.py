# so many list comprehensions (。_。)
from itertools import combinations, permutations
from math import isqrt

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

ban = [int("".join(x)) for x in permutations('1487')]
for i in range(1000, 10000):  # going up to 10000 is unnecessary but shouldn't decrease performance with an exit condition
    if i in ban or not isPrime(i):
        continue

    x = [x for x in str(i)]
    for y in combinations(permutations(x), 3):
        n = [int("".join(z)) for z in y]
        if isPrime(n[0]) and isPrime(n[1]) and isPrime(n[2]) and n[2] - n[1] == n[1] - n[0] and n[2] != n[1] !=n [0]:
            print("".join([str(x) for x in n]))
            quit()
