from math import factorial
from itertools import count

def combination(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

total = 0
for n in range(23, 101):
    # we can then ignore the outer 2 values as they won't exceed 100
    for k in range(2, n - 2):
        if combination(n, k) > 1000000:
            total += 1

print(total)