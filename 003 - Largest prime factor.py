n = 600851475143
while n > 1:
    temp = 2
    #just keep increasing temp until it divides cleanly
    while n % temp != 0:
        temp += 1
    n /= temp
    if n == 1:
        print(temp)