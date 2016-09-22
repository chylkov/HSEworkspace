# lst is a sorted list of numbers, x is a number
# returns minimal i, such that lst[i] > x
# note that result can be len(lst), if all elements of lst are <= x
# use binary search!

def lower_bound(lst, x):
    left, right = 0, len(lst) - 1
    while left < right - 1:
        middle = (left + right) // 2
        print('left', left, 'right', right, 'middle', middle)
        if x > lst[middle]:
            left = middle
        else:
            right = middle
        if left == right:
            return  left#len(lst)
        #else:
    print('end: ', 'left:', left, 'right', right, 'middle', middle)
    return left

# print(lower_bound([1, 2, 3, 4, 5, 6], 4)) #3
# print(lower_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 3)) #6


def upper_bound(lst, x):
    left, right = 0, len(lst) - 1
    while left < right:
        middle = (left + right) // 2
        #print('left', left, 'right', right, 'middle', middle)
        if x >= lst[middle]:
            left = middle + 1
        else:
            right = middle
        if left == right:
            return left
    #print('end: ', 'left:', left, 'right', right, 'middle', middle)
    return middle

# print(upper_bound([1, 2, 3, 4, 5, 6], 4)) #3
# print(upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 3)) #6

def test_upper_bound(lst, x):
  i = upper_bound(lst, x)
  print('answer is ', i)
  assert (i == len(lst) or lst[i] > x) and (i == 0 or lst[i - 1] <= x)

def small_tests():
  #test_upper_bound([1, 2, 3, 4, 5, 6], 4)
  #test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 3)
  #test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 2)
  #test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], -2)

  # THERE!
  #test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 6)
  # AND THERE!
  #test_upper_bound([1, 2, 3, 3, 3, 3, 3, 4, 6], 8)

  #test_upper_bound([3, 7, 12, 22, 47], 17)
  test_upper_bound([-200, -34, -5, 0, 45], -12)

def big_tests():
  lst = [i for i in range(0, 10 ** 6, 5)]
  test_upper_bound(lst, 3)
  test_upper_bound(lst, 45)
  test_upper_bound(lst, 10 ** 7)
  test_upper_bound(lst, -12)
  test_upper_bound(lst, 3454)
  test_upper_bound(lst, 23)
  test_upper_bound(lst, 324)
  test_upper_bound(lst, 10 ** 6 - 1)
  test_upper_bound(lst, 10 ** 6 - 5)
  test_upper_bound(lst, 0)

small_tests()
#big_tests()