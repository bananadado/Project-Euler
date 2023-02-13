# increase T by one as it increases the slowest
T = 285 + 1
P = 165
H = 143

while True:
    triangle = T*(T+1)/2
    pentagonal = P*(3*P-1)/2
    hexagonal = H*(2*H-1)
    minimum = min(triangle, pentagonal, hexagonal)
    if minimum == max(triangle, pentagonal, hexagonal):
        print(int(minimum))
        quit()

    if minimum == triangle:
        T += 1
    if minimum == pentagonal:
        P += 1
    if minimum == hexagonal:
        H += 1
