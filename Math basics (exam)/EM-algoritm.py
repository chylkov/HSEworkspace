import math
import random


def load_data():
    with open('data.txt', 'r') as inputfile:
        data_raw = inputfile.readlines()
    return [float(x) for x in data_raw]


def gauss(x, m, sigm):
    return math.exp(-(x-m) * (x-m) / (2 * sigm * sigm))/math.sqrt(2 * math.pi * sigm * sigm)


def probability(x, m1, m2, sigm, alpha):
    return alpha * gauss(x, m1, sigm) / (alpha * gauss(x, m1, sigm) + (1 - alpha)*gauss(x, m2, sigm))


def count_mean(data):
    if len(data) == 0:
        return 0
    return sum(data)/len(data)


def get_random_number():
    return random.random()


def error_count(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2)**2 + (z1 - z2)**2)


def update_array(a, param, value):
    if len(a) > param - 1:
        a.pop(0)
    a.append(value)
    return a


def em():
    data = load_data()
    alpha = 0.5
    sigma = 7
    error = 10
    current_girls_mean = 160
    current_boys_mean = 175
    girls_means = []
    boys_means = []
    alphas = []
    steps = 0
    param = 10

    while error > 0.3: #empirical
        current_girls = []
        current_boys = []

        for point in data:
            prob_value = probability(point, current_boys_mean, current_girls_mean, sigma, alpha)
            gen_value = get_random_number()
            if prob_value > gen_value:
                current_boys.append(point)
            else:
                current_girls.append(point)

        alpha = len(current_boys) / len(data)
        current_girls_mean = count_mean(current_girls)
        current_boys_mean = count_mean(current_boys)
        error = error_count(current_boys_mean, count_mean(boys_means), current_girls_mean, count_mean(girls_means), alpha, count_mean(alphas))

        update_array(girls_means, param, current_girls_mean)
        update_array(boys_means, param, current_boys_mean)
        update_array(alphas, param, alpha)

        steps += 1

    print('\nBoys mean: {0}\nGirls mean: {1}\nAlpha: {2}\nSteps: {3}'.format(current_boys_mean, current_girls_mean, alpha, steps))

# import matplotlib.pyplot as plt
# plt.plot(errors[1:])
# plt.show()

em()
