import math


def print_matrix(b):
    for row_id in range(len(b)):
        for column_id in range(len(b[0])):
            print(b[row_id][column_id], end="\t")
        print()
    print()


def generate_matrix(N,M, number):
    matrix = []
    last = number
    for i in range(N):
        row = []
        for j in range(M):
            row.append(last)
            if number != 0:
                last += 1
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


def add(m1, m2, empty):
    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        empty = generate_matrix(len(m1), len(m2[0]))
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                empty[i][j] = m1[i][j] + m2[i][j]
    else:
        print("Error: Несовпадающие размерности")


def translation(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            #if i < j: # условие для трансопнирования квадратной матрицы
                k = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = k


def normalize_rows(m):
    for i in range(0, len(m)):
        n = 0
        for j in range(0, len(m[0])):
            n += m[i][j] ** 2
        n = math.sqrt(n)
        for j in range(0, len(m[0])):
            m[i][j] /= n


def normalize_columns(m):
    for j in range(0, len(m[0])):
        n = 0
        for i in range(0, len(m)):
            n += m[i][j]**2
        n = math.sqrt(n)
        for i in range(0, len(m)):
            m[i][j] /= n


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

def triangle_1(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i <= j):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def triangle_2(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i >= j):
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def triangle_3(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i + j) < N:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def triangle_4(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if (i + j) >= N-1:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def norm1(a):
    norm = 0
    list_of_max = []
    for i in range(len(a)):
        line_sum = 0
        for j in range(len(a[0])):
            line_sum += a[i][j]
        list_of_max.append(line_sum)
    return max(list_of_max)


def norm_e(a):
    sq_sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sq_sum += a[i][j] * a[i][j]
    return math.sqrt(sq_sum)


# N, M = 2, 2
# A = generate_matrix(N, M, 1)
# B = generate_matrix(N, M, 2)
# print_matrix(A)
# print_matrix(B)
# C = generate_matrix(N, M, 0, True)

# add(A,B,C)
# print_matrix(C)

# translation(C)
# print_matrix(C)

# normalize_rows(C)
# print_matrix(C)

# D = generate_matrix(2, 3, 1)
# E = generate_matrix_identity(3)
# print_matrix(D)
# print_matrix(E)
# F = multiply(D,E)
# print_matrix(F)

#T = triangle_4(5)
#print_matrix(T)

G = generate_matrix(3, 4, 1)
print_matrix(G)
print(norm1(G))
print(norm_e(G))