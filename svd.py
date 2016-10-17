import math
import random


def generate_matrix(N,M, number):
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(number)
        matrix.append(row)
    return matrix


def generate_matrix_random(N, M):
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(random.random())
        matrix.append(row)
    return matrix


def generate_matrix_identity(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def multiply(a, b):
    if len(a[0]) != len(b):
        print("Error: Несовпадающие размерности")
        return
    N = len(a)
    M = len(b[0])
    K = len(a[0])
    r = generate_matrix(N, M, 0)
    for i in range(N):
        for j in range(M):
            for k in range(K):
                r[i][j] += a[i][k] * b[k][j]
    return r


def print_matrix(b):
    for row_id in range(len(b)):
        for column_id in range(len(b[0])):
            print(b[row_id][column_id], end="\t")
        print()


def error(a, b):
    sum_error = 0
    N = len(a)
    M = len(b[0])
    for i in range(N):
        for j in range(M):
            sum_error += (a[i][j] - b[i][j]) * (a[i][j] - b[i][j])
    #print('ERROR', sum_error)
    return sum_error


def norm_e(a):
    sq_sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sq_sum += a[i][j] * a[i][j]
    return math.sqrt(sq_sum)


def add(m1, m2):
    empty = generate_matrix(len(m1), len(m1[0]), 0) # add checking
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            empty[i][j] = m1[i][j] + m2[i][j]
    return empty


def number_multiply(a, number):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= number
    return a


def recount(a, u, l, v):
    a_new = multiply(multiply(u, l), v)
    u_new = generate_matrix(len(u), len(u[0]), 0)
    v_new = generate_matrix(len(v), len(v[0]), 0)
    l_new = generate_matrix(len(l), len(l[0]), 0)
    for i in range(len(u)):
        for k in range(len(u[0])):
            s = 0
            for j in range(len(v[0])):
                s += 2*(a[i][j]-a_new[i][j])*l[k][k]*v[k][j]
            u_new[i][k] = s
    for k in range(len(l)):
        sum = 0
        for i in range(len(u)):
            for j in range(len(v[0])):
                sum += 2*(a[i][j]-a_new[i][j])*u[i][k]*v[k][j]
        l_new[k][k] = sum
    for k in range(len(v)):
        for j in range(len(v[0])):
            sum = 0
            for i in range(len(u)):
                sum += 2*(a[i][j]-a_new[i][j])*l[k][k]*u[i][k]
            v_new[k][j] = sum
    return u_new, l_new, v_new


def svd(a, L, eps, e):
    epsilon = eps ** 2
    N = len(a)
    M = len(a[0])
    u = generate_matrix_random(N, L)
    l = generate_matrix_identity(L)
    v = generate_matrix_random(L, M)
    b = multiply(multiply(u, l), v)

    last = 0
    current = error(a, b)
    steps = 0
    while math.fabs(last - current) > epsilon:
        steps += 1
        u_new, l_new, v_new = recount(a, u, l, v)
        u = add(u, number_multiply(u_new, e))
        l = add(l, number_multiply(l_new, e))
        v = add(v, number_multiply(v_new, e))
        b = multiply(multiply(u, l), v)
        last = current
        current = error(a, b)

    print('Steps: ', steps)
    return u, l, v


def main():
    N = 3
    L = 2
    M = 3
    a = generate_matrix_random(N, M)
    print('Input matrix:')
    print_matrix(a)
    print('-'*9)
    u, l, v = svd(a, L,  10 ** (-4), 10 ** (-3))
    aa = multiply(multiply(u, l), v)
    print('Error: ', error(a, aa))
    print('-'*9 + '\nRecovered matrix:')
    print_matrix(aa)
    print('-'*9 + '\nMatrix U')
    print_matrix(u)
    print('-'*9 + '\nMatrix L')
    print_matrix(l)
    print('-'*9 + '\nMatrix V')
    print_matrix(v)

main()