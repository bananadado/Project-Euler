# since we just need to check patterns of up to 18 non-zero / zeroed digits, there are 2^18 combinations
# you can then just multiply each pattern by the number of possible digit combinations
# cache is like a bit of a broken ability we can just use and it just kinda works
# this should probably be difficulty 2 not 3 icl
from functools import cache

@cache
def win(pattern):
    for i in range(len(pattern)):
        remaining = pattern[:i] + pattern[i+1:]

        # strip leading zeroes
        j = 0
        while j < len(remaining) and remaining[j] == 0:
            j += 1
        remaining = remaining[j:]

        # empty => win
        # opponent doesn't win => win (remaining digits are non winning)
        if not remaining or not win(remaining):
            return True
    return False

t = 0
for d in range(1, 19):
    for mask in range(1 << (d - 1)):
        # build pattern - lead with 1
        # (this with the d-1 above guarantees a unique bit mask for the number of digits)
        pattern = tuple(int(c) for c in f"1{mask:0{d-1}b}")

        if win(pattern):
            t += 9 ** sum(pattern)

print(t)
