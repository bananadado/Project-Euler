from itertools import count
from math import isqrt

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for i in count(1):
        x = n - 2*i*i
        if x < 1:
            return False
        if isPrime(x):
            return True

for i in count(9, 2):
    if isPrime(i):
        continue
    if not goldbach(i):
        print(i)
        quit()