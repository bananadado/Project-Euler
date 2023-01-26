import math
def isMade(n):
    if n == sum(math.factorial(int(x)) for x in str(n)):
        return True
    return False
total = 0
for i in range(3, 10000000):
    if isMade(i):
        total += i
print(total)