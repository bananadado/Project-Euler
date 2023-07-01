def convergent(n):
    if n % 3 == 2:
        return 2 * (n // 3) + 2
    return 1

numerator = 2
denominator = 1

for i in range(1, 100):
    numerator, denominator = convergent(i) * numerator + denominator, numerator

print(sum(int(x) for x in str(numerator)))