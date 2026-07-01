# we need k st 2 * k(k-1) = n(n-1) for some n >= 10^12
# clearly 4 | n(n-1) => nothing at all i just thought of it :clown:
# the easiest approach is just to continuously increment k and n in turn
# the second easiest approach is just to increment k:
# so n^2 - n - 2k(k-1) = 0
# n = (1 + sqrt(1 + 8k(k-1))) / 2

# we need to use isqrt due to precision errors
# float sqrt is only exact below 2^53 (~9e15); 
# near the answer 1 + 8k(k-1) is ~1e23, so is_integer() is wrong

# this approach ran for ~1.75 days and it got the correct answer :D
# however, the "correct" approach i think is to use a Pell equation which i dont know yet but will get back to when i do the Diophantine problem.

from itertools import count
from math import isqrt

def solve(target):
  for k in count(2):
    d = 1 + 8 * k * (k - 1)
    s = isqrt(d)
    if s * s == d:
      n = (1 + s) // 2
      if n >= target:
        return k


print(solve(21))
print(solve(10**12))
