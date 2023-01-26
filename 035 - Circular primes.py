from math import isqrt


def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


total = 0
for i in range(2, 1000000):
    for j in range(len(str(i))):
        if not isPrime(int(str(i)[j:] + str(i)[:j])):
            break
        if j == len(str(i)) - 1:
            total += 1
print(total)
