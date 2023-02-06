from fractions import Fraction

numerator, denominator = 1, 1
print("The fractions because they are on a need-to-know basis:")

for i in range(10, 100):
    for j in range(i + 1, 100):
        #  we can ignore cancelling columns and only need to cancel diagonals
        n, d = str(i), str(j)
        if n[1] == "0" or d[1] == "0":
            continue

        fract1, fract2 = Fraction(1, 1), Fraction(1, 1)

        if n[0] == d[1]:
            fract1 = Fraction(int(n[1]), int(d[0]))
        if n[1] == d[0]:
            fract2 = Fraction(int(n[0]), int(d[1]))

        if fract1 == Fraction(i, j) or fract2 == Fraction(i, j):
            print(n+"/"+d)
            numerator *= i
            denominator *= j

print(f"\nAnswer: {Fraction(numerator, denominator).denominator}")
