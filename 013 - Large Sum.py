with open("013 - input.txt","r") as f:
    inp = [line for line in f.readlines()]

total = 0
for i in inp:
    total += int(i)

print(str(total)[0:10])