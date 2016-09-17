#divcount
import math

def divcount(n):
	count = 0
	if n == 1:
		return 1
	i = 1
	while i * i <= n:
		if (i * i == n):
			count += 1
		else:
			if n % i == 0:
				count += 2
		i += 1
	return count


def test_divcount(n, answer):
	assert divcount(n) == answer

test_divcount(1, 1)
test_divcount(5, 2)
test_divcount(121, 3)
test_divcount(10 ** 5, 36)
test_divcount(2 * 3 * 5, 8)
test_divcount(2 ** 7 * 5 ** 3 * 11, 64)
test_divcount(13 ** 3 * 41 ** 5, 24)
test_divcount(10 ** 9 + 7, 2)
test_divcount(10 ** 12 + 39, 2)