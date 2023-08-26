from itertools import count
from collections import defaultdict

digits = 0
counters = defaultdict(lambda: [float('inf'), 0])

for i in count():
    cubedDigits = "".join(str(x) for x in sorted([int(x) for x in str(i**3)]))
    if len(cubedDigits) > digits:
        for keys, data in counters.items():
            if data[1] == 5:
                print(data[0])
                quit()
        counters = defaultdict(lambda: [float('inf'), 0])
        digits = len(cubedDigits)
    counters[cubedDigits][0] = min(counters[cubedDigits][0], i**3)
    counters[cubedDigits][1] += 1
