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
            if (i == j):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def multiply(a, b):
    if (len(a[0]) != len(b)):
        print("Error: Несовпадающие размерности")
        return
    r = generate_matrix(len(a), len(b[0]), 0)
    N = len(a)
    M = len(b[0])
    K = len(a[0])
    """
    чтобы не вычислять каждый раз длину списка
    """
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
    print()

def error(a, b, N):
    sum_error = 0
    for i in range(N):
        for j in range(N):
            sum_error += (a[i][j] - b[i][j]) * (a[i][j] - b[i][j])
    #print('ERROR', sum_error)
    return sum_error


def norm_e(a):
    sq_sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sq_sum += a[i][j] * a[i][j]
    return math.sqrt(sq_sum)


def add(m1, m2, N):
    empty = generate_matrix(N, N, 0) # add checking
    for i in range(N):
        for j in range(N):
            empty[i][j] = m1[i][j] + m2[i][j]
    return empty


def number_multiply(a, number, N):
    for i in range(N):
        for j in range(N):
            a[i][j] *= number
    return a


def recount(a, u, l, v, N):
    a_new = multiply(multiply(u, l), v)
    u_new = generate_matrix(N, N, 0)
    v_new = generate_matrix(N, N, 0)
    l_new = generate_matrix(N, N, 0)
    for i in range(N):
        for k in range(N):
            s = 0
            for j in range(N):
                s += 2*(a[i][j]-a_new[i][j])*l[k][k]*v[k][j]
            u_new[i][k] = s
    for k in range(N):
        sum = 0
        for i in range(N):
            for j in range(N):
                sum += 2*(a[i][j]-a_new[i][j])*u[i][k]*v[k][j]
        l_new[k][k] = sum
    for k in range(N):
        for j in range(N):
            sum = 0
            for i in range(N):
                sum += 2*(a[i][j]-a_new[i][j])*l[k][k]*u[i][k]
            v_new[k][j] = sum
    return u_new, l_new, v_new


N = 3
u = generate_matrix_random(N, N)
l = generate_matrix_identity(N)
v = generate_matrix_random(N, N)
epsilon = 10 ** (-5)
e = 10 ** (-2)

a = generate_matrix_random(N, N) #3
b = multiply(multiply(u, l), v)
print_matrix(a)
print_matrix(b)
print(error(a, b, N))

steps = 0
while error(a, b, N) > epsilon:
    steps += 1
    u_new, l_new, v_new = recount(a, u, l, v, N)
    u = add(u, number_multiply(u_new, e, N), N)
    l = add(l, number_multiply(l_new, e, N), N)
    v = add(v, number_multiply(v_new, e, N), N)
    b = multiply(multiply(u, l), v)
    print('ERROOOR BETWEEN OLD U AND NEW U', error(u, u_new, N))
    print('ERROOOR BETWEEN OLD L AND NEW L', error(l, l_new, N))
    print('ERROOOR BETWEEN OLD V AND NEW V', error(v, v_new, N))

print('steps', steps, '\n')
aa = multiply(multiply(u, l), v)
print(aa)
print('-'*9)
print(a)
