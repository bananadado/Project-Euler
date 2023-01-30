for c in range(500):
    for b in range(c):
        for a in range(b):
            if a**2+b**2 == c**2 and a+b+c == 1000:
                print(a*b*c)
                quit
