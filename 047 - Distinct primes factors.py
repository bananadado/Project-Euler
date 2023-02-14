# takes about a minute
from itertools import count

def primeFactors(n):
    factors = set()
    while n != 1:
        for i in count(2):
            if n % i == 0:
                for j in count(1):
                    n //= i
                    if n % i != 0:
                        factors.add(i**j)
                        break
                break
    return factors

cache = [primeFactors(647), primeFactors(648), primeFactors(649)]
for i in count(647):
    f1, f2, f3 = cache[0], cache[1], cache[2]
    f4 = primeFactors(i+3)

    cache.pop(0)
    cache.append(f4)

    if len(f1) != 4 or len(f2) != 4 or len(f3) != 4 or len(f4) != 4:
        continue

    if len(f1.union(f2, f3, f4)) == 16:
        print(i)
        quit()
