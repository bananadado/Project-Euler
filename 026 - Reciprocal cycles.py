longest = 0
longestNum = 0
for i in range(1,1000):
    length = 0
    seenRemainders = []
    remainder = 1
    while(True):
        seenRemainders.append(remainder)
        remainder = (remainder * 10) % i
        if remainder in seenRemainders:
            length = len(seenRemainders) - seenRemainders.index(remainder)
            break
    if length > longest:
        longest = length
        longestNum = i

print(longestNum)
