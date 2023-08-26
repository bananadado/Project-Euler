values = [x for x in "23456789TJQKA"]
valueDictionary = {r: i for i, r in enumerate(values)}
ranks = [[3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

with open("054 - poker.txt", "r") as f:
    hands = [line.split() for line in f.readlines()]


def royalFlush(hand):
    royal = len(set([x[0] for x in hand]).intersection(set(values[::-1][:5]))) == 5
    return royal and flush(hand)


def straightFlush(hand):
    suit = len(set([x[1] for x in hand])) == 1
    return straight(hand) and flush(hand)


def flush(hand):
    return len(set([x[1] for x in hands])) == 1


def straight(hand):
    cardValues = [valueDictionary[x[0]] for x in hand]
    return sorted(cardValues) == list(range(min(cardValues), max(cardValues) + 1))


def evalHand(hand):
    cards = [x[0] for x in hand]
    cardSort = sorted([(x, cards.count(x)) for x in list(set(cards))], key=lambda x: (x[1], valueDictionary[x[0]]))[::-1]
    handRank = [0, [valueDictionary[x[0]] for x in cardSort], [x[1] for x in cardSort]]

    if royalFlush(hand):
        return handRank
    handRank[0] -= 1
    if straightFlush(hand):
        return handRank
    handRank[0] -= 1

    # Four of a kind
    if handRank[2] == [4, 1]:
        return handRank
    handRank[0] -= 1

    # Full house
    if handRank[2] == [3, 2]:
        return handRank
    handRank[0] -= 1

    if flush(hand):
        return handRank
    handRank[0] -= 1

    if straight(hand):
        return handRank
    handRank[0] -= 1

    for i in range(4):
        if handRank[2] == ranks[i]:
            return handRank
        handRank[0] -= 1


def choose(num1, num2):
    if num1 > num2:
        return 1
    if num1 < num2:
        return 2
    return 0


def evalScore(hand1, hand2):
    hand1Eval = evalHand(hand1)
    hand2Eval = evalHand(hand2)

    if choose(hand1Eval[0], hand2Eval[0]) != 0:
        return choose(hand1Eval[0], hand2Eval[0])
    for i in range(len(hand1Eval[1])):
        if choose(hand1Eval[1][i], hand2Eval[1][i]) != 0:
            return choose(hand1Eval[1][i], hand2Eval[1][i])


scores = [0, 0]
for x in hands:
    scores[evalScore(x[:5], x[5:]) - 1] += 1
print(scores[0])
