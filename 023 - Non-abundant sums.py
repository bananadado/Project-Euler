import math

abundantNums = []


def factorise(num):
    factorTotal = 1
    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            if i == math.sqrt(num):
                factorTotal += math.sqrt(num)
            else:
                factorTotal += i
                factorTotal += num/i
    return factorTotal


for i in range(1, 28124):
    if factorise(i) > i:
        abundantNums.append(i)

abundantTotals = set()
for i in abundantNums:
    for j in abundantNums:
        if i+j < 28124:
            abundantTotals.add(i+j)
        else:
            break
total = 0
for i in range(1, 28124):
    if not(i in abundantTotals):
        total += i
print(total)
