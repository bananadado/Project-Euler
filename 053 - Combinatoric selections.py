from math import factorial
from itertools import count

def combination(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))

# we are going to find a place to start searching from first
start = 0
for i in count(2):
    if combination(i, i//2) > 1000000:
        start = i
        break

total = 0
for n in range(start, 101):
    # we can then ignore the outer 2 values as they won't exceed 100
    for k in range(2, n - 2):
        if combination(n, k) > 1000000:
            total += 1

print(total)