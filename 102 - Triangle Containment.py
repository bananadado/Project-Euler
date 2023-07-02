ORIGIN = (0, 0)
coords = []
with open("102 - triangles.txt", "r") as f:
    for x in f.readlines():
        temp = [int(y) for y in x.split(",")]
        coords.append([(temp[0], temp[1]), (temp[2], temp[3]), (temp[4], temp[5])])


area = lambda a, b, c: abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2

# using area
def isInside(a, b, c):
    return area(a, b, c) == area(a, b, (0, 0)) + area(a, c, (0, 0)) + area(c, b, (0, 0))


print(len([s for s in coords if isInside(s[0], s[1], s[2])]))
