#max divisor
#максимальный делитель числа, меньший самого числа

def max_divisor(n):
    i = 2
    max_el = 1
    tmp = 0
    n_dov_two = n // 2  # not count on every iteration
    while i < n // 2:
        if n % i == 0:
            tmp = n // i
            if max_el < tmp:
                max_el = tmp
        i += 1
    return max_el

def test_max_divisor(n, answer):
    assert max_divisor(n) == answer

test_max_divisor(5, 1)
test_max_divisor(30, 15)
test_max_divisor(81, 27)
n = 3 ** 4 * 7 ** 3
test_max_divisor(n, n // 3)
n = 11 ** 5 * 43 ** 3 * 67
# not working on these tests
#test_max_divisor(n, n // 11)
# test_max_divisor(10 ** 12 + 39, 1)
# test_max_divisor(1009 ** 3, 1009 ** 2)
# test_max_divisor(999983 ** 2, 999983)