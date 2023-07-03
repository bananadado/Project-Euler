# could've utilised memoization but the problem is simple enough not to
from math import factorial as f
from itertools import count

terms = set()
total = 0

for i in range(4, 1000000):
    term = i
    terms.add(i)
    for j in count(1):
        if j > 60:
            break
        term = sum([f(int(x)) for x in str(term)])
        if term in terms:
            if j == 60:
                total += 1
            break
        terms.add(term)
    terms.clear()

print(total)
