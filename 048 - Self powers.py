# like the multiplication problem, all we need to do is keep the last ten digits
n = 0
for i in range(1, 1001):
    n = int(str(n + i**i)[-10:])
print(n)