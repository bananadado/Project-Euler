# Farey Sequence
def countFareyTerms(n=12000):
    (a, b, c, d) = (0, 1, 1, n)

    counter = 0
    while c <= n:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)

        if a/b == 1/2:
            return counter

        if a/b > 1/3:
            counter += 1

print(countFareyTerms())