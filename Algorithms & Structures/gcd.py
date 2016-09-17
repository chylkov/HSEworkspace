# gcd

import math

def gcd(a, b):
    print('enter recursive call, a =', a, 'b =', b)
    if b == 0:
        print(a)
        return a
    else:
        return gcd(b, a % b)

def test_gcd(a, b):
    assert gcd(a, b) == math.gcd(a, b)
    print()

test_gcd(2, 3)
test_gcd(81, 27)
test_gcd(10 ** 7, 10 ** 11)
test_gcd(123456, 12345678)
test_gcd(10 ** 12 + 39, 999983)
test_gcd(12586269025, 7778742049) # Fib_50, Fib_49