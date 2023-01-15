import math

seen = set()

def factorise(num):
    factorTotal = 1
    for i in range(2, round(math.sqrt(num))):
        if num%i == 0:
            if i == math.sqrt(num):
                factorTotal += math.sqrt(num)
            else:
                factorTotal += i
                factorTotal += num/i
    return factorTotal

for num in range(2,10000):
    if num in seen:
        continue

    if factorise(factorise(num)) == num and factorise(num) != num and factorise(num) < 10000:
        seen.add(num)
        seen.add(factorise(num))


print(int(sum(seen)))
