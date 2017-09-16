import random
import numpy as np

#0 - решка
#1 - орел
eagle = 1

def shake_shaker(n):
    results = []
    for i in range(n):
        take = random.randint(0,1)
        results.append(take)
    return results


def count_sequence(seq):
    count_max = 1
    current = 1
    last = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == last and seq[i] == eagle:
            current += 1
            if current > count_max:
                count_max = current
        else:
            current = 1
        last = seq[i]
    return count_max


def count_switches(seq):
    count = 0
    last = seq[0]
    for i in range(1, len(seq)):
        if seq[i] != last:
            count += 1
        last = seq[i]
    return count

n = 100
max_eagles = []
all_swithes = []
experiment = 2000
for i in range(experiment):
    takes = shake_shaker(n)
    eagles = count_sequence(takes)
    switches = count_switches(takes)
    max_eagles.append(eagles)
    all_swithes.append(switches)

print(np.mean(switches))
print(np.mean(all_swithes))
