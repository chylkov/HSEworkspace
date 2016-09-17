import math

m = [[1, 3], [2, 7]]
#e_list = [10 ** (-2), 10 ** (-3), 10 ** (-4), 10 ** (-5), 10 ** (-6), 10 ** (-7)]
a1, a2, b1, b2 = 0, 1, 3, 4
epsilon = 10 ** (-9)


def derivative_by_a1(a1, a2, b1, b2):
    return 2 * b1 * (a1 * b1 - 1) + 2 * b2 *(a1 * b2 - 3)


def derivative_by_a2(a1, a2, b1, b2):
    return 2 * b1 * (a2 * b1 - 2) + 2 * b2 * (a2 * b2 - 7)


def derivative_by_b1(a1, a2, b1, b2):
    return 2 * a1 * (a1 * b1 - 1) + 2 * a2 * (a2 * b2 - 2)


def derivative_by_b2(a1, a2, b1, b2):
    return 2 * a1 * (a1 * b2 - 3) + 2 * a2 * (a2 * b2 - 7)


def count_function_error(a1, a2, b1, b2):
    return (a1*b1 - 1)*(a1*b1 - 1) + (a1*b2 - 3)*(a1*b2 - 3) + (a2*b1 - 2)*(a2*b1 - 2) + (a2*b2 - 7)*(a2*b2 - 7)


def check(a1, a2, b1, b2):
    print('E: {0}'.format(e))
    print('Matrix: ')
    print('{0}    {1}'.format(a1 * b1, a1 * b2))
    print('{0}    {1}'.format(a2 * b1, a2 * b2))


def grad(e, a1, a2, b1, b2):
    error = count_function_error(a1, a2, b1, b2)
    previous_error = error + 0.1
    step = 0
    while previous_error - error > epsilon:
        previous_error = error
        a1 -= e * derivative_by_a1(a1, a2, b1, b2)
        a2 -= e * derivative_by_a2(a1, a2, b1, b2)
        b1 -= e * derivative_by_b1(a1, a2, b1, b2)
        b2 -= e * derivative_by_b2(a1, a2, b1, b2)
        error = count_function_error(a1, a2, b1, b2)
        #print('current error = {0}, previous error = {1}, diff = {2}'.format(error, previous_error, error - previous_error))
        #print('STEP = {0}, a1 = {1}, a2 = {2}, b1 = {3}, b2 = {4}'.format(step, a1, a2, b1, b2))
        step += 1

    #print('-' * 45)
    check(a1, a2, b1, b2)
    print('Steps: ', step)
    print('Answer: ', end='')
    print('a1 = {}, a2 = {}, b1 = {}, b2 = {}'.format(a1, a2, b1, b2))
    l = count_function_error(a1, a2, b1, b2)
    print(l)
    print('-' * 45)

e = 10 ** (-2)
while e > 10 ** (-7):
    a1, a2, b1, b2 = 0, 1, 3, 4
    grad(e, a1, a2, b1, b2)
    e /= 2
    l = count_function_error(a1, a2, b1, b2)
    print(l)

