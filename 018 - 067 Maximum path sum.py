with open("018 - 067 p67.txt","r") as f:
    inp = [[int(x) for x in line.strip().split(' ')] for line in f.readlines()]
print(inp)
for i in range(len(inp) - 2, -1, -1):
    for j in range(len(inp[i])):
        inp[i][j] = max(inp[i][j] + inp[i + 1][j], inp[i][j] + inp[i + 1][j +1])
print(inp[0][0])