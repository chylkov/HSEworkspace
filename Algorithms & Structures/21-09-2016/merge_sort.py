import random

# left, right are sorted lists of numbers
# returns sorted list, containing numbers from left and right
def merge(left, right):
    tmp = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            tmp.append(left[0])
            left.pop(0)
        else:
            tmp.append(right[0])
            right.pop(0)
    tmp += left
    tmp += right
    return tmp

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst) // 2
    left_sorted = merge_sort(lst[:middle])
    right_sorted = merge_sort(lst[middle:])
    res = merge(left_sorted, right_sorted)
    return res

#print(merge_sort([6, 5, 4, 3, 2, 1]))

def test_merge_sort(lst):
    assert merge_sort(lst) == sorted(lst)

def small_tests():
      test_merge_sort([1, 2, 3, 4, 5, 6])
      test_merge_sort([6, 5, 4, 3, 2, 1])
      test_merge_sort([46, 76, 23, 6, 2345, 4, 87, 4, 4, 4, 456])
      test_merge_sort([5])
      test_merge_sort([23, 56, 12, 6, 2, 6, 1, 56, 123])

def big_tests():
      lst = list(range(10 ** 4))
      for i in range(10):
        random.shuffle(lst)
        test_merge_sort(lst)

small_tests()
big_tests()
