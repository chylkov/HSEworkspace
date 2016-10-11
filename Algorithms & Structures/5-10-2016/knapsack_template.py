
# We want to store in knapsack with given capacity
# items with maximum overall cost.
# Code is for variant of problem, where cost = weight
# It is sufficient to change only ONE line of code.
def knapsack_cost(weights, costs, capacity):
  n = len(weights)
  best = [0] * (capacity + 1)
  for i in range(1, n + 1):
    for j in range(capacity, 0, -1):
      if j >= weights[i - 1]:
        best[j] = max(best[j], best[j - weights[i - 1]] + costs[i - 1]) #учитываем цену
  return best[capacity]

# We want to store in knapsack with given capacity
# items with maximum overall weight. We can
# take every item _infinite_ times.
# Code is for variant of problem, where we can
# take every item only once.
# It is sufficient to change only ONE line of code.
def knapsack_infinite(weights, capacity):
  n = len(weights)
  best = [0] * (capacity + 1)
  for i in range(1, n + 1):
      for j in range(capacity, 0, -1):
          k = 1
          while j >= k*weights[i - 1]: #пока влезает в рюкзак
              best[j] = max(best[j - k*weights[i - 1]] + k*weights[i - 1], best[j])
              k += 1
  return best[capacity]

def test_cost():
  assert knapsack_cost ([1, 3, 5], [1, 3, 5], 7) == 6
  assert knapsack_cost ([2, 2, 5], [3, 3, 5], 6) == 6
  assert knapsack_cost ([1, 1, 1, 4], [2, 2, 2, 7], 4) == 7
  assert knapsack_cost ([23, 5, 3, 12, 7], [34, 2, 7, 9, 21], 40) == 64
  assert knapsack_cost ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 15) == 15
  assert knapsack_cost ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 14) == 14
  assert knapsack_cost ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 7) == 12
  assert knapsack_cost ([5], [10], 33) == 10
  assert knapsack_cost ([5, 6], [10, 6], 14) == 16

def test_infinite():
  assert knapsack_infinite ([1, 3, 5], 7) == 7
  assert knapsack_infinite ([2, 2, 5], 6) == 6
  assert knapsack_infinite ([1, 1, 1, 4], 4) == 4
  assert knapsack_infinite ([23, 5, 3, 12, 7], 40) == 40
  assert knapsack_infinite ([1, 2, 3, 4, 5], 15) == 15
  assert knapsack_infinite ([1, 2, 3, 4, 5], 14) == 14
  assert knapsack_infinite ([1, 2, 3, 4, 5], 7) == 7
  assert knapsack_infinite ([5], 33) == 30
  assert knapsack_infinite ([5, 6], 14) == 12

#test_cost()
test_infinite()