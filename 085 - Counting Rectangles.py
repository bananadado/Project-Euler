# For any Nx1 grid, there will be the corresponding triangle number of rectangles: N(N+1)/2
# If expanded to an Nx2 grid, there will be the same amount of rectangles as an Nx1 grid added, plus the same amount again of 2xM rectangles: 3N(N+1)/2
# This pattern follows for any NxM grid, where the coefficient at the front is also a triangle number, resulting in the formula:
# (M(M+1)/2)(N(N+1)/2) = N*(N+1)*M*(M+1)/4 for the number of rectangles in any NxM grid
# This can be proved by combinatorics, where 2 distinct horizontal and vertical lines are chosen to form a rectangle:
# (N+1)_C_2 * (M+1)_C_2 = ((N+1)!/(N-1)!2!)*((M+1)!/(M-1)!2!) = (N(N+1)/2)(M(M+1)/2) = N*(N+1)*M*(M+1)/4 :)

# Now all is left is to get as close as we can to 2000000 with any integer N, M
from math import isqrt, prod

rectangles = lambda N, M: N * (N + 1) * M * (M + 1) / 4

TARGET = 2000000
combos = ((n, m) for n in range(1, isqrt(TARGET) + 1) for m in range(1, isqrt(TARGET) + 1))
print(prod(min(combos, key=lambda x: abs(rectangles(x[0], x[1]) - TARGET))))
