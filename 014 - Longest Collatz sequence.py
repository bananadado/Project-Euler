scores = []

# not very efficient but uhm
for i in range(2, 1000000):
    current = [i]
    while current[len(current) - 1] != 1:
        current.append(current[len(current) - 1]/2 if current[len(current) - 1] % 2 == 0 else current[len(current) - 1]*3 + 1)
    scores.append(len(current))

print(scores.index(max(scores)) + 2)