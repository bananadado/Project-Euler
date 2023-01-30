# dies
ones = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
tens = {0: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

total = 0
for i in range(1, 1001):
    n = str(i).zfill(4)
    if i == 1000:
        total += len("onethousand")
    if n[1] != "0":
        total += len(ones[int(n[1])] + "hundred" + ("and" if n[2:] != "00" else ""))
    if n[2] == "1":
        total += len(teens[int(n[3])])
    else:
        total += len(tens[int(n[2])] + ones[int(n[3])])
print(total)