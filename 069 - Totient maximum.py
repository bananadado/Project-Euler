def totientList(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result

totientRatio = [i/j for i, j in enumerate(totientList(1000002)) if j > 0]
print(totientRatio.index(max(totientRatio)) + 1)   #  +1 as we ignore 0
