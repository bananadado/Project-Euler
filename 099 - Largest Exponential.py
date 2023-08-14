import math
hLine, hBase, hExp = 0, 1, 0

with open("099 - base exp.txt", "r") as f:
    for i, pair in enumerate(f.readlines()):
        base, exp = int(pair.split(',')[0]), int(pair.split(',')[1])
        if exp * math.log10(base) >= hExp * math.log10(hBase):
            hLine, hBase, hExp = i + 1, base, exp

print(hLine)
