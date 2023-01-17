#top right = n^2
#top left = n^2 - (n-1)
#bottom left = n^2 - 2(n-1)
#bottom right = n^2 - 3(n-1)
#total for each spiral = 4n^2 - 6(n-1)
total = 1
for n in range(3, 1002, 2):
    total += 4*(n**2) - 6*(n - 1)
print(total)