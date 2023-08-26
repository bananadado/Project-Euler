# Dynamic programming partition problem - partition numbers
# https://en.wikipedia.org/wiki/Partition_(number_theory)
GOAL = 100
numbers = range(1, GOAL)
ways = [1] + [0]*GOAL

for n in numbers:
    for i in range(n, GOAL+1):
        ways[i] += ways[i-n]

print(ways[GOAL])
