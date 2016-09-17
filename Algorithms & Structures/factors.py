def factors(n):
    result = []
    i = 1
    while i <= n:
        if n % i == 0 and is_prime(i):
            result.append(i)
            n = n // i
            i = 1
        i += 1
    print(result)
    return result

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def mul(lst):
    result = 1
    for x in lst:
        result *= x
    return result
    # could be replaced by
    # return functools.reduce(lambda x, y: x * y, lst, 1)

def test_factors(n):
    n_factors = factors(n)
    assert mul(n_factors) == n
    for x in n_factors:
        assert is_prime(x)
    # could be replaced by
    # assert all([is_prime(x) for x in n_factors])

test_factors(1)
test_factors(2)
test_factors(5)
test_factors(10)
test_factors(81)
test_factors(10 ** 6)
test_factors(7 ** 3 * 43 ** 4 * 67 ** 2)
test_factors(10 ** 12 + 39)
test_factors(2 ** 50)
test_factors(2 ** 10 * 3 ** 20)