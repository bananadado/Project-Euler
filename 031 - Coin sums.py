# for for loops are four, for twice you shall for read this statement; for
total = 0
for one in range(201):  # you can fit 200 pennies into £2, so you make it so that it can be counted from 0-200
    for two in range(101):
        if one + two*2 > 200:
            break
        for five in range(41):
            if one + two * 2 + five * 5 > 200:
                break
            for ten in range(21):
                if one + two * 2 + five * 5 + ten * 10 > 200:
                    break
                for twenty in range(11):
                    if one + two * 2 + five * 5 + ten * 10 + twenty*20 > 200:
                        break
                    for fifty in range(5):
                        if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 > 200:
                            break
                        for hundred in range(3):
                            if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred*100 > 200:
                                break
                            for twoHundred in range(2):
                                if one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred*100 + twoHundred * 200 == 200:
                                    total += 1
print(total)