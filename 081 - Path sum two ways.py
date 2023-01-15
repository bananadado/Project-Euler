#somehow i coded this all in one go and it ran first try correctly without bugs
from collections import deque

matrix = []
with open("081 - input.txt","r") as f:
    for line in f.readlines():
        inp = line.split(',')
        matrix.append(list(map(int, inp)))

matrixValues = []
for _ in range(len(matrix)):
    temp = []
    for __ in range (len(matrix)):
        temp.append(2e20)
    matrixValues.append(temp)

low = 2e20
seen = set()

q = deque()
q.append((0,0,matrix[0][0]))

while(q):
    x, y, total = q.popleft()

    if x == len(matrix) - 1 and y == len(matrix) - 1:
        if total < low:
            low = total
        continue

    if (x,y) in seen:
        if total >= matrixValues[x][y]:
            continue
    seen.add((x,y))
    matrixValues[x][y] = total

    if x < len(matrix) - 1:
        q.append((x + 1, y, matrix[x+1][y] + total))
    if y < len(matrix) - 1:
        q.append((x, y + 1, matrix[x][y+1] + total))

print(low)
