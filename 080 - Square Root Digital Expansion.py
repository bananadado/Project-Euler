# Check every number 2-99
# If it is a square, ignore
# Else, multiply by 100^Digits (as 100 is square and doesn't "affect" the digits) and get the square root of it which is then truncated and added together
from math import isqrt
print(sum(sum(int(x) for x in str(isqrt(y * 100 ** 100))[:100]) for y in range(2, 100) if isqrt(y)**2 != y))
