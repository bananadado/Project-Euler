# This problem can be done with either: Prim's or Kruskal's Algorithm
with open("107  - network.txt", "r") as f:
    network = [[int(x) if x != '-' else 0 for x in line.strip().split(',')] for line in f.readlines()]

totalWeight = int(sum([sum(row) for row in network])/2)
network = [[int(x) if x != 0 else float('inf') for x in line] for line in network]

# We will use Prim's as Kruskal's requires a sort and labelling of the network, even if it is slightly more simple
runningWeight = 0
visited = {0}
for i in range(len(network) - 1):
    currentMin = float('inf')
    currentCol = 0
    for j in visited:
        for k, value in enumerate(network[j]):
            if value < currentMin and k not in visited:
                currentMin = value
                currentCol = k
    runningWeight += currentMin
    visited.add(currentCol)

print(totalWeight - runningWeight)
