"""
for each digit length:
 - enumerate possible digit-pair sums.
 - simulate carry chain
 - count valid combinations (multiplicatively)
"""
from itertools import product

def count_reversible(d):
    m = d // 2
    is_odd = d % 2 == 1

    # count (a,b) pairs giving each sum
    # outer pair: a,b >= 1 (no leading zeros)
    outer = {}
    for a in range(1, 10):
        for b in range(1, 10):
            s = a + b
            outer[s] = outer.get(s, 0) + 1

    # inner pairs: a,b >= 0
    inner = {}
    for a in range(10):
        for b in range(10):
            s = a + b
            inner[s] = inner.get(s, 0) + 1

    # middle digit (odd d): sum = 2a
    middle = {}
    for a in range(10):
        middle[2 * a] = middle.get(2 * a, 0) + 1

    # enumerate all pair-sum tuples
    pair_counts = [outer if k == 0 else inner for k in range(m)]
    pair_sums = [list(pc.keys()) for pc in pair_counts]
    mid_sums = list(middle.keys()) if is_odd else [None]

    total = 0
    for sums in product(*pair_sums):
        for ms in mid_sums:
            carry = 0
            ok = True

            # right half: columns 0..m-1
            for k in range(m):
                val = sums[k] + carry
                if val % 2 == 0:  # digit must be odd
                    ok = False
                    break
                carry = val // 10

            if not ok:
                continue

            # middle column (odd d)
            if is_odd:
                val = ms + carry
                if val % 2 == 0:
                    ok = False
                if not ok:
                    continue
                carry = val // 10

            # left half: same sums in reverse
            for k in range(m - 1, -1, -1):
                val = sums[k] + carry
                if val % 2 == 0:
                    ok = False
                    break
                carry = val // 10

            if not ok:
                continue

            # carry=1 means extra leading digit of 1 (odd, fine)
            ways = 1
            for k in range(m):
                ways *= pair_counts[k][sums[k]]
            if is_odd:
                ways *= middle[ms]
            total += ways

    return total

print(sum(count_reversible(d) for d in range(1, 10)))