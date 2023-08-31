from itertools import count
from math import isqrt

LIMIT = 10**12
repunits = set()

for i in range(2, isqrt(LIMIT) + 1):
    current = i + 1
    for j in count(2):
        current += i**j
        if current > LIMIT:
            break
        repunits.add(current)
print(sum(repunits) + 1)
