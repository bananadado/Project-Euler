# Just look at all combinations, up to sqrt(10^8) = 10^4
from itertools import count

total = set()
for i in range(1, 10**4 + 1):
    currentSum = i * i
    for j in count(i + 1):
        currentSum += j * j

        if currentSum >= 10**8:
            break

        if str(currentSum) == str(currentSum)[::-1]:
            total.add(currentSum)

print(sum(total))