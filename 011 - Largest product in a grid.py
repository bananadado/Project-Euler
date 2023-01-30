from math import prod
with open("011 - input.txt", "r") as f:
    n = [[int(x) for x in i.strip().split()] for i in f.readlines()]

highest = 0
for row in range(len(n)):
    for column in range(row):
        if row < len(n) - 3:
            highest = max(prod([n[row][column], n[row + 1][column], n[row + 2][column], n[row + 3][column]]), highest)
            if column < row - 3:
                highest = max(prod([n[row][column], n[row + 1][column + 1], n[row + 2][column + 2], n[row + 3][column + 3]]), highest)
            if column > 2:
                highest = max(prod([n[row][column], n[row + 1][column - 1], n[row + 2][column - 2], n[row + 3][column - 3]]), highest)
        if column < row - 3:
            highest = max(prod([n[row][column], n[row][column + 1], n[row][column + 2], n[row][column + 3]]), highest)

print(highest)