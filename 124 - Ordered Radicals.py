from sympy import primefactors
from math import prod

rad = [prod(primefactors(x)) for x in range(1, 100001)]
paired = [[i, r] for i, r in enumerate(rad)]
print(sorted(paired, key=lambda x: x[1])[9999][0] + 1)
