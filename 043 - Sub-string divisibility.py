from itertools import permutations
PRIMES = [2, 3, 5, 7, 11, 13, 17]

def isDivisible(n):
    for i in range(7):
        if int(n[i+1] + n[i+2] + n[i+3]) % PRIMES[i] != 0:
            return False
    return True

print(sum([int("".join(x)) for x in permutations(list("0123456789")) if isDivisible("".join(x))]))
