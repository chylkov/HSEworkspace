#largest_square_divisor

import math

def largest_square_divisor(n):
    result = 1
    i = 1
    while i * i <= n:
        if n % (i * i) == 0 and i > result:
            result = i
        i += 1
    return result

def test_largest_square_divisor(n, answer):
    assert largest_square_divisor(n) == answer

test_largest_square_divisor(999999937 ** 2, 999999937)
#test_largest_square_divisor(999999937 * (10 ** 9 + 7), 1)
# test_largest_square_divisor(8, 2)
# test_largest_square_divisor(75, 5)
# test_largest_square_divisor(999983 ** 3, 999983)
# test_largest_square_divisor(999979 * 999983 ** 2, 999983)
# test_largest_square_divisor(999979 * 999983, 1)
# test_largest_square_divisor(999961 * 999979 * 999983, 1)