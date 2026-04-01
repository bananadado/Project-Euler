# we just use euler's totient function on all numbers
# use a sieve of Eratosthenes
# runs in O(nloglogn)

def solve(limit=1_000_000):
    phi = list(range(limit + 1))  # phi[i] = i
    for p in range(2, limit + 1):
        if phi[p] == p: # prime
            # since phi[m] = n prod_(p|n)(1 - 1/p)
            # stepwise:
            # phi[m] = phi[m] * (1 - 1/p)
            # phi[m] = phi[m] - phi[m] / p
            for m in range(p, limit + 1, p):
                phi[m] -= phi[m] // p
    return sum(phi[2:])

print(solve())