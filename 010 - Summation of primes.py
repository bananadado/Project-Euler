from math import isqrt


def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


print(sum([x for x in range(2, 2000000) if isPrime(x)]))
