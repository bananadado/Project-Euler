from itertools import count, islice
from math import isqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def isTruncablePrime(n):
    o = str(n)
    for i in range(len(o)):
        if not isPrime(int(o[i:])):
            return False
        if not isPrime(int(o[:i + 1])):
            return False
    return True


print(sum(islice(filter(isTruncablePrime, count(10)), 11)))
