from itertools import count
def isTriangularWord(word):
    wordNum = sum([ord(l)-64 for l in word])
    # now we iterate through the triangle numbers
    t = 0
    for i in count():
        t += i
        if t > wordNum:
            return False
        if t == wordNum:
            return True

with open("042 - words.txt", "r") as f:
    print(len([w for w in f.readline().split(",") if isTriangularWord(w.strip("\""))]))

