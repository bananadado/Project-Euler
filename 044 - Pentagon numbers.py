# This solution is horribly brute force (took 59.296875s to run on my pc)
# I will come back and make a new solution if I get time
from itertools import count
D = set()

def sumPent(n1, n2):
    # making use of python's weird way of being able to use variables from out of scope
    if n1+n2 in PNUMS:
        return True
    return False

def differencePent(n1, n2):
    if abs(n1 - n2) in PNUMS:
        return True
    return False

# we are going to check intervals of 2000 numbers, increasing by 200 each time
for j in count(0, 200):
    PNUMS = [i * (3 * i - 1) / 2 for i in range(j+1, j + 2000)]
    for i, n1 in enumerate(PNUMS):
        for n2 in PNUMS[i:]:
            if sumPent(n1, n2) and differencePent(n1, n2):
                D.add(abs(n1-n2))

    if len(D) > 0:
        print(int(min(D)))
        quit()
