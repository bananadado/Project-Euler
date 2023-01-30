from math import isqrt, sqrt
from itertools import count

def numDivisors(n):
    s = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            s.add(i)
            if i != sqrt(n):
                s.add(n / i)
    return len(s)

for i in count():
    if numDivisors(int(0.5*i*(i+1))) > 500:
        print(int(0.5*i*(i+1)))
        break