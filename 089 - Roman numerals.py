numeralToNum = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
numToNumeral = {v: k for k, v in numeralToNum.items()}


def generateRomanNumeral(n):
    num = n
    output = ""
    while num > 0:
        for v in numToNumeral.keys():
            if v <= num:
                num -= v
                output += numToNumeral[v]
                break

            if num >= 900:
                num -= 900
                output += "CM"
                break
            if v == 500 and num >= 400:
                num -= 400
                output += "CD"
                break
            if v == 100 and num >= 90:
                num -= 90
                output += "XC"
                break
            if v == 50 and num >= 40:
                num -= 40
                output += "XL"
                break
            if num == 9 or num == 4:
                num = 0
                output += "I" + numToNumeral[num + 1]
                break
    return output


def decodeRomanNumeral(s):
    numeral = s
    n = 0
    while numeral:
        if len(numeral) > 1:
            if numeralToNum[numeral[1]] > numeralToNum[numeral[0]]:
                n += numeralToNum[numeral[1]] - numeralToNum[numeral[0]]
                numeral = numeral[2:]
                continue
        n += numeralToNum[numeral[0]]
        numeral = numeral[1:]
    return n


with open("089 - roman.txt", "r") as f:
    print(sum([len(n.strip()) - len(generateRomanNumeral(decodeRomanNumeral(n.strip()))) for n in f.readlines()]))
