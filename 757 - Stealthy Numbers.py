# mmm pronic numbers:

# a+b=c+d+1, ab=cd=N
# Let s = c + d
# => a + b = s + 1
# so a, b roots of x^2 - (s + 1)x + N = 0
# similarly, c, d roots of x^2 - sx + N = 0
# we need integer solutions so discriminant is perf. square:
# s^2 - 4N = k^2, (s+1)^2 - 4N = m^2; k, m ∈ Z
# => m^2 - k^2 = 2s + 1
# => (m + k)(m - k) = 2s + 1
# 2s + 1 odd => m + k, m - k odd
# Let p = m + k = 2i + 1, q = m - k = 2j + 1; i, j ∈ Z, p >= q
# 4N = s^2 - k^2
# s = (pq - 1) / 2, k = (q - p) / 2
# => 4N = (p - 1)(q + 1)(p + 1)(q - 1) / 4
# => N = i(i+1) * j(j+1)

# so we need to count all pairs of pronic numbers such that N < 10^14
# there's like 10^8 products probably so probably can just numpy things and pray
# also the answer is surprisingly related to the problem number lol

import numpy as np
from math import isqrt

LIMIT = 10**14

pronic = lambda x: x * (x + 1)

chunks = []
for i in range(1, isqrt(LIMIT)):
    ip = pronic(i)
    if ip * ip > LIMIT:
        break

    # max j s.t. pronic(i) * pronic(j) <= LIMIT
    # pronic(j) <= LIMIT / pronic(i)
    # j^2 + j - bound <= 0
    bound = LIMIT // ip
    j_max = int((-1 + (1 + 4 * bound) ** 0.5) / 2)

    # i -> j avoid duplicating entries (saves ~<half memory)
    j = np.arange(i, j_max + 1, dtype=np.int64)
    products = ip * pronic(j)
    chunks.append(products)

# find distinct in computable time (no set)
all_products = np.concatenate(chunks)
all_products.sort()
print(1 + np.count_nonzero(np.diff(all_products))) # n - 1 entries from diff => + 1