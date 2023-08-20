# Runs in 40s or so, not the most efficient but likely won't come back to fix it unless another problem builds on it
from collections import defaultdict
from itertools import permutations, count

# Already nicely formatted 😎 #emojiCoding
with open("098 - words.txt", "r") as f:
    words = eval(f.readline())

# Create a dictionary of all words belonging to a group of anagrams
anagrams = defaultdict(list)
for word in words:
    anagrams["".join(sorted(word))].append(word)

# Computing this means we now know the length of the squares we must compute up to
maxSize = max(len(x) for x in anagrams.keys() if len(anagrams[x]) > 1)

# Create the list categorised by length then the number of unique digits
squares = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
for i in count():
    stri = str(i ** 2)
    if len(stri) > maxSize:
        break
    squares[len(stri)][len(set(stri))]["".join(sorted(stri))].append(stri)

# remove all lists less than 2 in length
for (key, values0) in squares.items():
    for (key2, values) in values0.items():
        temp = defaultdict(list)
        for (sort, items) in values.items():
            if len(items) > 1:
                temp[sort] = items
        squares[key][key2] = temp


# Checks if a number (sorted) and a word (sorted) have the same amount of occurrences of the same amount of things
def pairs(sortedWord, currentKey):
    currentChar = sortedWord[0]
    currentNum = currentKey[0]
    for i in range(len(sortedWord)):
        if (currentChar == sortedWord[i]) ^ (currentNum == currentKey[i]):
            return False
        currentChar = sortedWord[i]
        currentNum = currentKey[i]
    return True


# Finds the maximum score of 2 words within an anagram set
# Finds all unique permutations of a word and then checks if that words "pairs" up with a number in the squares dict
def findMaxPair(sortedWord, word1, word2) -> int:
    currentMaxSquare = 0
    permutes = ["".join([y * sortedWord.count(y) for y in x]) for x in permutations(list(set(sortedWord)))]
    for (key, values) in squares[len(sortedWord)][len(set(sortedWord))].items():
        for letterCombo in permutes:
            if pairs(letterCombo, key):
                mapping = {}
                for i in range(len(sortedWord)):
                    mapping[key[i]] = letterCombo[i]
                mappedWords = ["".join(mapping[l] for l in x) for x in values]
                if word1 in mappedWords and word2 in mappedWords:
                    # print(f"{currentMaxSquare}, {word1} : {int(values[mappedWords.index(word1)])}, {word2} : {int(values[mappedWords.index(word2)])}")
                    currentMaxSquare = max(currentMaxSquare, int(values[mappedWords.index(word1)]), int(values[mappedWords.index(word2)]))

    return currentMaxSquare


currentMax = 0
for (key, values) in anagrams.items():
    # print(f"{key}: {list(anagrams.keys()).index(key)}/{len(anagrams)}")
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            currentMax = max(currentMax, findMaxPair(key, anagrams[key][i], anagrams[key][j]))

print(currentMax)
