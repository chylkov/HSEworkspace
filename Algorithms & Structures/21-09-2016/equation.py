import math

# finds x: x = cos(x)
# use binary search!
def solve_equation():
    left, right = -100, 100
    epsilon = 10 ** (-7)
    while left <= right - epsilon:
        middle = (left + right) / 2
        y = middle - math.cos(middle)
        #print('middle {0}, left {1}, right {2}, y {3}'.format(middle, left, right, y))
        if y < 0:
            left = middle
        else:
            right = middle
    return middle

x = solve_equation()
print(x, math.cos(x), abs(x - math.cos(x)))