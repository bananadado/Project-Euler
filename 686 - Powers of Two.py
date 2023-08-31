# There is another way to do this with strings but it is slightly more inefficient
from math import log10

LB, UB = log10(1.23), log10(1.24)
TARGET = log10(2)

total = 0
n = 0
while total < 678910:
    n += 1
    log = n * TARGET  # where n is the exponent of 2: log10(2^n) = nlog10(2)
    # If 2^n begins with '123' then the value of 0.abcde... (in nlog10(2) = x.abcde...) must be between log10(1.23) and log10(1.24)
    if LB < log - int(log) < UB:
        total += 1
print(n)
