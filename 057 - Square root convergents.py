total = 0
numerator = 0
denominator = 1

for _ in range(1000):
    # we are going to work out the latter half of the fraction (i.e. without the 1 +)
    numerator, denominator = denominator, denominator * 2 + numerator

    # then to compare the numerator and denominator we simply add the denominator to the numerator (adding the 1 + back)
    if len(str(numerator + denominator)) > len(str(denominator)):
        total += 1

print(total)
