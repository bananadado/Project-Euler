count = 0
result89 = set()
result1 = set()
for i in range(1, 10000000):
    temp = i
    tempSet = set([temp])
    while True:
        temp = sum([int(x)**2 for x in str(temp)])
        if temp in result1 or temp == 1:
            result1.update(tempSet)
            break
        if temp in result89 or temp == 89:
            result89.update(tempSet)
            break
        tempSet.add(temp)

print(len(result89))
