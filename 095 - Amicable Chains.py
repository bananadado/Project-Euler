from itertools import count

# Generate the divisor sum of all numbers, sieve-style :D
# Works the same as a sieve of eratosthenes but doesn't square i and looks at all the numbers 😉 #emojiCoding
properDivisors = [0]*1000001
for i in range(1, len(properDivisors)):
    for j in range(i * 2, len(properDivisors), i):
        properDivisors[j] += i

longestChain = 0
smallestChainNum = 0
for i in range(len(properDivisors)):
    visited = set()
    current = i
    for j in count():
        visited.add(current)
        proximal = properDivisors[current]

        # done a full loop back to i
        if i == proximal:
            if j > longestChain:
                longestChain = j
                smallestChainNum = i  # no need to check for min as j will only exceed longestChain once per chain
            break

        # there is a chain, but i isn't in it or the next number exceeds the limit of 1 million
        if proximal in visited or proximal > 1000000:
            break
        current = proximal
print(smallestChainNum)
