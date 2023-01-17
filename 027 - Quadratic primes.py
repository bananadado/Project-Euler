import math
import itertools

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

product = 0
highest = 0
# First we need to generate primes
# This alg isn't very efficient
primelist = []
sub1000 = []
count = 2
while(len(primelist) < 100000):
    if isPrime(count):
        primelist.append(count)
        if count <= 1000:
            sub1000.append(count)
    count += 1

primes = set(primelist)

# now that we have primes we are going to test all the quadratics MWHAHHAHAHA
#even though I have optimised the number theory a bit it is still quite slow
for a in range(-999, 1000, 2):  # a is likely odd
    for b in sub1000:  # as we are counting 0, b must be prime
        if not(1+a+b in primes):  # 1+a+b must be prime
            continue
        for x in itertools.count():
            if not((x*x + a*x + b) in primes):
                if x > highest:
                    highest = x
                    product = a*b
                break

print(product)

