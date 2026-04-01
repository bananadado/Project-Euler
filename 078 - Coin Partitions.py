# bro euler is actually just all over these problems
# Euler's pentagonal number theorem
# should be like O(nsqrt(n))

from itertools import count

MOD = 1_000_000

def pentagonal():
    # generate pentagonal numbers from k=1,-1,2,-2...
    g = lambda k: k * (3 * k - 1) // 2

    # include sign
    sgn = 1
    for i in count(1):
        yield sgn, g(i)
        yield sgn,g(-i)
        sgn *= -1

# build up list iteratively
p = [1, 1] # p(0) = 1, p(1) = 1

for n in count(2):
    t = 0

    for sgn, i in pentagonal():
        if i > n:
            break

        t += sgn * p[n - i]

    if t % MOD == 0:
        print(n)
        break

    p.append(t)