from math import isqrt
from itertools import count

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

c = 0
for i in count(2):
    if isPrime(i):
        c += 1
        if c == 10001:
            print(i)
            break