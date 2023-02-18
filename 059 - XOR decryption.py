#  we are just looking for a file with the most amount of lowercase letters
with open("059 - cipher.txt", "r") as f:
    ciphertext = [int(x) for x in f.readline().split(",")]

currentMax = 0
currentMaxKey = ""
currentMaxText = ""

for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            iterator = [a, b, c]
            plaintext = []
            for i, j in enumerate(ciphertext):
                plaintext.append(j ^ iterator[i % 3])

            # Now we're going to give this a score; +2 for a lowercase / space, +1 for an uppercase, +0 for anything else
            score = 0
            for x in plaintext:
                if 97 <= x < 123 or x == 32:
                    score += 2
                elif 65 <= x < 91:
                    score += 1

            if score > currentMax:
                currentMax = score
                currentMaxKey = "".join([chr(x) for x in iterator])
                currentMaxText = "".join([chr(x) for x in plaintext])

print(f"Answer: {sum([ord(x) for x in currentMaxText])}")
print(f"Key: {currentMaxKey}")
print(f"Message: {currentMaxText}")
