# "Hello Google my best friend...". or at least that's how i thought the song went
# Found something on stack overflow which helped but I had to do some maths :p
# So the nth digit of 1/x is floor(10**n/x)%10
# So I tried this... and it didn't work because too big 😭 #emojiCoding
# So I found this cool website called "Google" and did some research.
# 10**n = 10*10**(n-1)   ...obviously
# 10**(n-1) = xq + r
# => 10**n = 10xq + r
# => 10**n/x = 10q + 10r/x
# => (10**n/x)%10 = 10r/x      which is then floored with //

def d(n, x):
    return (10 * pow(10, n - 1, x)) // x

print(sum([d(10**7, k) for k in range(1, 10**7 + 1)]))
