import random

# lst is a list of numbers
# returns sorted version of lst
# just replace None's and pass with appropriate code
def counting_sort(lst):
  count = [0] * (max(lst) + 1)
  for x in lst:
  	count[x] += 1
  result = []
  for i in range(len(count)):
    for j in range(count[i]):
      result.append(i)
  return result

def test_counting_sort(lst):
  assert counting_sort(lst) == sorted(lst)

def small_tests():
  test_counting_sort([1, 2, 3, 4, 5, 6])
  test_counting_sort([6, 5, 4, 3, 2, 1])
  test_counting_sort([46, 76, 23, 6, 2345, 4, 87, 4, 4, 4, 456])
  test_counting_sort([5])
  test_counting_sort([23, 56, 12, 6, 2, 6, 1, 56, 123])

def big_tests():
  lst = list(range(10 ** 4))
  for i in range(10):
    random.shuffle(lst)
    test_counting_sort(lst)

small_tests()
big_tests()