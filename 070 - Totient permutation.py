def totientList(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result

totients = totientList(10**7 - 1)
ans = 0
ratio = float('inf')
for i, totient in enumerate(totients[2:], 2):  # start at 2 to remove zero division errors
    if i/totient < ratio and sorted(str(i)) == sorted(str(totient)):
            ratio = i/totients[i]
            ans = i
print(ans)
