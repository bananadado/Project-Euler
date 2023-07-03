from itertools import count

def checkBouncy(n):
    increase = False
    decrease = False
    nlist = [int (x) for x in str(n)]
    for i in range(1, len(nlist)):
        if nlist[i] < nlist[i - 1]:
            decrease = True
        elif nlist[i] > nlist[i - 1]:
            increase = True
        if increase == True and decrease == True:
            return increase
    return False

bouncy = 0
for i in count(100):
    if checkBouncy(i):
        bouncy += 1
        if bouncy/i == 0.99:
            print(i)
            quit()
