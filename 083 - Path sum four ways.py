# simple bfs type search. runs effectively immediately
from collections import deque

distance = [[2e20]*80 for i in range(80)]
matrix = []
with open("083 - matrix.txt", "r") as f:
    for line in f.readlines():
        matrix.append(list(map(int, line.split(','))))

q = deque()
q.append((matrix[0][0], 0, 0))
distance[0][0] = matrix[0][0]
while q:
    total, row, col = q.popleft()

    if total > distance[row][col] or total > distance[79][79]:
        continue

    #right
    if col < 79 and total + matrix[row][col + 1] < distance[row][col + 1]:
        q.append((total + matrix[row][col + 1], row, col+1))
        distance[row][col + 1] = total + matrix[row][col + 1]
    #left
    if col > 0 and total + matrix[row][col - 1] < distance[row][col - 1]:
        q.append((total + matrix[row][col - 1], row, col-1))
        distance[row][col - 1] = total + matrix[row][col - 1]
    #down
    if row < 79 and total + matrix[row + 1][col] < distance[row + 1][col]:
        q.append((total + matrix[row + 1][col], row + 1, col))
        distance[row + 1][col] = total + matrix[row + 1][col]
    #up
    if row > 0 and total + matrix[row - 1][col] < distance[row - 1][col]:
        q.append((total + matrix[row - 1][col], row - 1, col))
        distance[row - 1][col] = total + matrix[row - 1][col]

print(distance[79][79])
