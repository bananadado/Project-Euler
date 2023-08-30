# x, y < n => x = n + p, y = n + q
# 1/(n+p) + 1/(n+q) = 1/n
# n/(n+p) + n/(n+q) = 1
# n(n+q) + n(n+p) = (n+q)(n+p)
# 2n^2 + nq + np = n^2 + nq + np + pq
# n^2 = pq
# The number of solutions must be equal to the amount of (combinations of p and q + 1)/2
# (+1 as we include the unique solution of n)
# The solution must have a high number of factors, so we generate it the same way as problem 500

# I've spent hours attempting to optimise it for part II but nothing worked ;-;

from math import isqrt
from itertools import count

# function from problem 047 :D
def numDivisors(n):
    total = 1
    escape = isqrt(n)
    for i in count(2):
        if i > escape:
            break
        if n % i == 0:
            j = 0
            while True:
                n //= i
                j += 1
                if n % i != 0:
                    break
            total *= j*2 + 1
            escape = isqrt(n)
    return total * 3 if n != 1 else total


for i in count():
    if (numDivisors(i) + 1)/2 >= 1000:
        print(i)
        quit()

