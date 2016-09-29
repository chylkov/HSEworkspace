import random

# lst is a list of numbers, n is a number
# returns sorted(lst)[n] without sorting lst
# there are no big tests, but please implement O(n) algorithm
# just replace None's and NotImplemented's with appropriate code
def nth_element(lst, n):
  if len(lst) == 1:
    return lst[0]
  pivot = random.choice(lst)
  less = [x for x in lst if x < pivot]
  equal = [x for x in lst if x == pivot]
  greater = [x for x in lst if x > pivot]
  #print('n', n)
  #print('pivot', pivot)
  #print('less', less)
  #print('equal', equal)
  #print('greater', greater)
  if len(less) > n:
    return nth_element(less, n)
  elif len(less) + len(equal) > n:
    return equal[0]
  else:
    return nth_element(greater, n - len(less) - len(equal))

def test_nth_element(lst, n, answer):
  assert nth_element(lst, n) == answer

def small_tests():
  test_nth_element([8, 5, 3, 1], 1, 3)
  test_nth_element([2, 8, 4, 6], 2, 6)
  test_nth_element([23, 675, 13, 57, 6], 0, 6)

def random_test():
  lst = list(range(100))
  random.shuffle(lst)
  n = random.choice(lst)
  test_nth_element(lst, n, n)

def test_equal():
  lst = [1] * 100
  for i in range(100):
    test_nth_element(lst, i, 1)

def medium_tests():
  test_equal()
  for i in range(20):
    random_test()

small_tests()
medium_tests()
#print(nth_element([8, 5, 3, 1], 1))
#print(nth_element([2, 8, 4, 6], 2))