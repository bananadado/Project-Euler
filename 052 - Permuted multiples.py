from itertools import count

for i in count(1):
    nums = [set(list(str(i * j))) for j in range(1, 7)]
    if nums[0] == nums[1] == nums[2] == nums[3] == nums[4] == nums[5]:
        print(i)
        quit()
