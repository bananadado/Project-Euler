seen = set()
for a in range(2,101):
    for b in range(2, 101):
        if not (a**b in seen):
            seen.add(a**b)
print(len(seen))
