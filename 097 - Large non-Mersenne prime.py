n = 1
for _ in range(7830457):
    #we only need the last 10 digits throughout because multiplication
    n = int(str(n*2)[-10:])

n*=28433
n+=1
print(str(n)[-10:])
