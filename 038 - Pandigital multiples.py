ans = ""
for i in range(2, 10):
    for j in range(1, 10**(9//i)):  # This exponent will limit the amount of permutations there are
        temp = "".join([str(x*j) for x in range(1, i + 1)])
        if "".join(sorted(temp)) == "123456789":
            ans = max(ans, temp)

print(ans)
