total = 0
for i in range(10000):
    n = i
    for j in range(50):
        n += int(str(n)[::-1])
        if n == int(str(n)[::-1]):
            total += 1
            break

print(10000-total)