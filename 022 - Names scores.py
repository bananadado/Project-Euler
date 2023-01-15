with open("022 - names.txt","r") as f:
    names = [name.strip("\"") for name in f.readline().split(',')]
names.sort()
total = 0
for i, name in enumerate(names):
    temptotal = 0
    chars = list(name)
    for char in chars:
        temptotal += ord(char) - 64
    total += temptotal*(i+1)

print(total)