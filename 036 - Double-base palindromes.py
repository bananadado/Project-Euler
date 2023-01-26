def isPalindrome(n):
    if n == n[::-1]:
        return True
    return False

total = 0
for i in range(1000000):
    if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
        total += i

print(total)