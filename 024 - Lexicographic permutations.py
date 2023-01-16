from itertools import permutations
#itertools will perform permutations lexicographically given the input order
perms = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
print(''.join(perms[999999]))
