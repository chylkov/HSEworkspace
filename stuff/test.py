p1 = 0.5
p2 = 0.5000001
q1 = 1 - p1
q2 = 1 - p2

import math

n = ((2 * 1.28 * math.sqrt(p1*q1)) / (p1 - p2)) ** 2

print(round(n))