from math import isqrt

# a list of all string 1 digit numbers because I can't count
EXIST = [str(x) for x in range(10)]

def isPrime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def generatePrimes(limit):
    # Sieve of Eratosthenes
    arr = [True] * (limit + 1)
    for i in range(2, isqrt(limit)):
        if arr[i]:
            for j in range(i**2, limit + 1, i):
                arr[j] = False
    return [x for x, prime in enumerate(arr) if prime and x > 1]


primes = generatePrimes(10000000)  # we are going to assume its below 1 million

for num in primes:
    splitNum = list(str(num))

    # first we are going to iterate through every number 0-9 and check if it is in num
    for each in EXIST:
        if each not in splitNum:
            continue

        # as it exists, we are going to try replacing it with every number
        notPrime = 0
        for n in EXIST:
            temp = []

            # if the number we are going to be replacing it with is 0, and the number we are replacing is at the start of the number, we must skip this
            if n == "0" and splitNum.index(each) == 0:
                notPrime += 1
                continue
            for i in splitNum:
                if i == each:
                    temp.append(n)
                else:
                    temp.append(i)

            # if the number we have created is not prime, we are going to add this to our counter
            if not isPrime(int("".join(temp))):
                notPrime += 1
            if notPrime > 2:
                break

        if notPrime <= 2:
            print(num)
            quit()
