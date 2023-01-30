fib = [1,2]
while fib[len(fib) - 1] < 4000000:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
print(sum([i for i in fib if i%2 == 0]))