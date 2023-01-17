total = 0
for i in range(2, 1000000):
    if sum(int(n)**5 for n in str(i)) == i:
        total += i
print(total)