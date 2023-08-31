from collections import deque

with open("345 - matrix.txt", "r") as f:
    matrix = [[int(y) for y in x.strip().split()] for x in f.readlines()]

# First subtract the largest value away
maxMatrix = max([max(x) for x in matrix])
inverse = [[maxMatrix - y for y in x] for x in matrix]

# Basically just do a dfs from every row (slightly more efficient than a bfs as it finds a max faster)
currentMin = float('inf')
currentMaxPath = []
for i in range(len(inverse[0])):
    q = deque()
    # running sum, visited rows, rows to visit
    q.appendleft((inverse[i][0], [i], [x for x in range(0, len(matrix)) if x != i]))

    while q:
        total, visited, toVisit = q.popleft()

        if len(toVisit) == 0 and total < currentMin:
            currentMin = total
            currentMaxPath = visited

        if total > currentMin:
            continue

        for j in range(len(toVisit)):
            if total + inverse[toVisit[j]][len(visited)] < currentMin:
                q.appendleft((total + inverse[toVisit[j]][len(visited)], visited + [toVisit[j]], toVisit[:j] + toVisit[j + 1:]))

print(sum([matrix[currentMaxPath[x]][x] for x in range(len(matrix))]))
