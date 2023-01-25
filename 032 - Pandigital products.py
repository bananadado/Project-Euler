from math import isqrt
def isPandigitalProductMaybe(n):
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            if "".join(sorted(str(i)+str(n//i)+str(n))) == "123456789":
                return True

total = 0
for i in range(1, 10000):  # 10000 because any 5 digit number would exceed 99^2 and therefore need more digits than available
    if isPandigitalProductMaybe(i):
        total += i
print(total)