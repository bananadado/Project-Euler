# Advent of Code 2022. the monkey one near the start where you do the modulus thing

# The 500500th prime is 7,376,507 according to https://t5k.org/nthprime/index.php#nth
# We know that the number is made up of primes, so we just construct it using primes 😎 #emojiCoding
# Every time it is multiplied by a prime, we can do the modulus thing just like that AoC problem as it doesn't matter in the end
# We are just trying to create a number using the smallest prime combo possible

from math import isqrt
from heapq import heappop, heappush

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]

primes = generatePrimes(7376507)
currentPrime = 0

# q will be a priority queue (using min binary heap) to serve up the smallest prime each time (refer to previous comment)
q = [primes[currentPrime]]

num = 1
for i in range(500500):
    # every time the element is popped it is the next smallest prime or prime square
    element = heappop(q)
    num = (num * element) % 500500507

    # Load in the next prime into the queue
    # This reminds me of that meme where queue is the perfect example of itself as "ueue" is just sitting there, waiting to be pronounced
    if element == primes[currentPrime]:
        currentPrime += 1
        heappush(q, primes[currentPrime])

    heappush(q, element*element)  # Flameded recently discovered that this is significantly faster than using the power function

print(num)
