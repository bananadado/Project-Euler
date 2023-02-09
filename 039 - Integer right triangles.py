from collections import defaultdict
import math

totals = defaultdict(lambda: 0)
for b in range(1000):
    for a in range(1, b):
        c = math.sqrt(a * a + b * b)
        if c % 1 == 0 and a+b+c <= 1000:
            totals[a+b+c] += 1

print(int(sorted(totals.items(), key=lambda x: x[1], reverse=True)[0][0]))
