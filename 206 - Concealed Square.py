# the square has 19 digits of which the first digit is 1 which restricts the domain to:
# 1000000000 <= x <= 1414213562
# The last digit is zero which restricts it to a multiple of 10

SEARCH = "1_2_3_4_5_6_7_8_9_0"

for i in range(1000000000, 1414213562, 10):
    n = str(i**2)
    found = True
    for j in range(0, 20, 2):
        if SEARCH[j] != n[j]:
            found = False
            break

    if found:
        print(i)
        quit()

