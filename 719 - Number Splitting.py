# an not optimal solution to the problem. I will revise this once I have completed 100 problems as this took 2 hours to run
import math
from itertools import count

def sieveOfSquares(maximum):
    squares = []
    for n in count():
        if n**2 > maximum:
            break
        squares.append(n**2)
    return squares

def split(n):
    possibilities = []
    nstr = str(n)
    if len(nstr) == 2:
        return [[int(x) for x in [nstr[0], nstr[1]]]]

    for i in range(1, len(nstr)):
        possibilities.append([int(x) for x in [nstr[:i], nstr[i:]]])
        for solution in split(nstr[i:]):
            possibilities.append([int(x) for x in [nstr[:i]] + solution])

    return possibilities

def isS(n):
    root = int(math.sqrt(n))
    if n < 10:
        return False

    # go through all permutations with 1 number at the start, then 2, then 3, etc.
    for i in split(n):
        if sum(i) == root:
            return True
    return False

print(sum(s for s in sieveOfSquares(10**12) if isS(s)))