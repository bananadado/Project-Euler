# originally tried a bfs type search but it was too slow so forced to abstract the problem
# distance is a 2D array that will store the current distance at every node
distance = [[0] * 80 for i in range(80)]
matrix = []
with open("082 - matrix.txt", "r") as f:
    for line in f.readlines():
        matrix.append(list(map(int, line.split(','))))

def distanceAtLoc(row, col):
    if col < 0:
        return 0
    elif row < 0 or row >= 80 or col >= 80:
        return float("inf")
    return distance[row][col]

for col in range(80):
    # Look at each node while going down the matrix
    # Make it the lowest it can be by looking back a column or by looking up a row
    #   - if it is the top row it can only look back due to the infinity value returned in the function above
    for row in range(80):
        distance[row][col] = matrix[row][col] + min(distanceAtLoc(row - 1, col), distanceAtLoc(row, col - 1))
    # All values in the column are now filled in.
    # Start again from the bottom of the column and look down, if the row below + node value is smaller than the other two (looking from above and left), use this instead
    for row in range(80)[::-1]:
        distance[row][col] = min(matrix[row][col] + distanceAtLoc(row + 1, col), distance[row][col])

print(min(distance[row][-1] for row in range(80)))
