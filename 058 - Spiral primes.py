# why did they rotate the spiral it was fine in problem 28
# top right = n^2 - 3(n-1)
# top left = n^2 - 2(n-1)
# bottom left = n^2 - (n-1)
# bottom right = n^2  => this diagonal doesn't need to be searched as it will never be prime
from math import isqrt
from itertools import count

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

primes = 0
total = 1

for i in count(3, 2):
    total += 4

    if isPrime(i ** 2 - (i - 1)):
        primes += 1
    if isPrime(i ** 2 - 2*(i - 1)):
        primes += 1
    if isPrime(i ** 2 - 3*(i - 1)):
        primes += 1

    if primes / total < 0.1:
        print(i)
        quit()
