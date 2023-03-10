count = 0
# valid numbers to have an exponent must lie in the range 1<= x < 10
# 9 has the most numbers that fit this pattern as it is the closest number to 10
# (which barely doesn't follow this rule by 1 digit)
# We just need to find the value of i in which 9^i is too small which happens to be 21

for i in range(1, 22):
    for j in range(1, 10):
        if len(str(j**i)) == i:
            count += 1
print(count)
