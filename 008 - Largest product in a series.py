from math import prod
with open("008 - input.txt", "r") as f:
    inp = [int(i) for x in f.readlines() for i in x.strip()]
print(max(prod(inp[i-13:i]) for i in range(13, len(inp))))