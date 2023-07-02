# took a lot of experimenting to realise that the difference between terms is simply 4503599627370517 % 1504170715041707
# when the difference is greater than the term, the new difference is d%term

sumOfTerms = 0
d = 4503599627370517 % 1504170715041707
currentTerm = 1504170715041707

while currentTerm > 0:
    sumOfTerms += currentTerm
    if currentTerm < d:
        d %= currentTerm
    currentTerm -= d

print(sumOfTerms)
