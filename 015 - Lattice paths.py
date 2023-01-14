# It is just combinatorics - 2n choose n
# Not very good explanation:
# This is because on an n*n grid, there is 2n amount of moves that the thing would do
# However, as you get closer towards the goal, there is a larger amount possible paths, but as you get further, it retreats to 1
# And here, if you notice, is Pascal's triangle - the number we are looking for would be on the 400th row, in the centre
# so we just need an algorithm for 40Choose20 (use calculator)
import math
print(int(math.factorial(40)/(math.factorial(20)*math.factorial(40-20))))
