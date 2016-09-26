import math

# finds x: x = cos(x)
# use binary search!
def solve_equation():
    left, right = -100, 100
    epsilon = 10 ** (-7)
    while left <= right - epsilon:
        middle = (left + right) / 2
        y = middle - math.cos(middle) #our function
        if y < 0:
            left = middle
        else:
            right = middle
    return middle

x = solve_equation()
print(x, math.cos(x), abs(x - math.cos(x)))