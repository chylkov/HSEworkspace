# In[25]:

# Самостоятельная работа по занятию: интегрирование методом трапеций
# Даны элементарная функция и интервал, на котором она неотрицательна.
# Разбить отрезок на равные интервалы. Вычислив значение ф. в середине отрезка каждого интервала,
# перемножить "высоту столбца" (от нуля до значения ф.) и его ширину (длину отрезка). Получим площадь.
# Сложив площади всех столбцов, получим приближение площади под графиком.
# Увеличивая число шагов деления интервала, постепенно уточняем значение площади под графиком.
# Когда модуль разности между двумя последовательными приближениями станет менее eps, 
# надо остановиться и распечатать итог: чему равна площадь и за сколько шагов мы её вычислили.

def task1():
    import math
    interval = (-1, 1)
    f = lambda x: -x ** 2 + 1
    eps = 0.000001
    step = 1
    current = 0
    previous = 0.1
    while math.fabs(current - previous) > eps:
        step += 1
        previous = current
        current = 0
        piece = (interval[1] - interval[0]) / step
        for i in range(step):
            current += math.fabs(f(interval[0] + i * piece / 2)) * piece

    print('Square is: ', current)
    print('Step is: ' , step)


# In[31]:

# Самостоятельная работа по занятию: интегрирование методом трапеций
# То же задание -- вычислить интеграл, но иным методом.
# Разбить отрезок на равные интервалы. В точках, по которым разбит отрезок, 
# вычислить значение, "соединить их отрезками".
# Просуммировав площади трапеций, как в предыдущей задаче, получим приближённую площадь под графиком.
# -- || --

def task2():
    interval = (-1, 1)
    f = lambda x: -x ** 2 + 1
    eps = 0.000001
    current = 0.1
    previous = 0
    step = 0
    while math.fabs(current - previous) > eps:
        step += 1
        previous = current
        h = (interval[1] - interval[0]) / step
        current = 0
        for i in range(step):
            current += h * (math.fabs(f(interval[0] + i * h)) + math.fabs(f(interval[0] + (i + 1) * h))) / 2

    print('Square is: ', current)
    print('Step is: ' , step)


# In[72]:

# Самостоятельная работа aka Задача [4]
# Запрограммировать интерполяционный многочлен Лагранжа (см. вики)
# 1) Взять у преподавателя элементарную функцию и вычислить её значения в нескольких точках, 
#    равномерно распределённых на некотором отрезке, и разбить пары (координата, значение в ней) 
#    на два массива в случайном порядке
# 2) Для разного количества точек и для разных точек строить многочлен и вычислять погрешность приближения -
#    например как сумму квадратов разностей ожидаемых значений и приближенных
# 3) Что наблюдаете и почему?


def task3():
    import math
    interval = (1.0, 10.0)
    f = lambda x: math.log(x, 2)
    step = 10
    steps = [10, 50, 100, 200, 500]
    errors = []
    sq_error = 0
    point = 10.0
    for step in steps:
        coord = []
        values = []
        lagrange_polinom = 0
        piece = (interval[1] - interval[0]) / step

        # заполнение массива точек и значений
        for i in range(step):
            coord.append(interval[0] + i * piece)
            values.append(f(interval[0] + i * piece))

        # формирование многочлена Лагранжа
        for i in range(step):
            tmp = 1
            for j in range(step):
                if i != j:
                    tmp *= (point - coord[j]) / (coord[i] - coord[j])
            lagrange_polinom += tmp * values[i]

        print('step:', step)
        print('my answer:', lagrange_polinom)
        print('right:',math.log(point, 2))
        print('*'*9)
        errors.append(lagrange_polinom - math.log(point, 2)) #подсчет ошибок

    for i in range(len(steps)):
        print('Step = {0}, error = {1}'.format(steps[i], errors[i]))


# In[ ]:

# Самостоятельная работа aka Задача 3
# Реализовать метод Гаусса решения СЛАУ [нужен рассказ о методе -- сигнальте].
# Считаем, что решение у СЛАУ есть, случай тривиальный.
# 1 Сгенерировать матрицу коэффициентов и констант.
# 2 Найти решение методом Гаусса.
# 3 Подставить решение и убедиться, что всё верно.

def print_matrix(b):
    for row_id in range(len(b)):
        for column_id in range(len(b[0])):
            print(b[row_id][column_id], end="\t")
        print()
    print(12*'*')


def generate_matrix(N, M, number):
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


def generate_vector(n, number):
    v = []
    q = number
    for i in range(n):
        if number == 0:
            v.append(0)
        else:
            q += 1
            v.append(q)
    return v


def multiply(a, b):
    if (len(a[0]) != len(b)):
        print("Error: Не совпадают размерности")
        return
    r = generate_vector(len(a[0]), 0)
    N = len(a[0])
    for i in range(N):
        s = 0
        for k in range(N):
            s += a[i][k] * b[k]
        r[i] = s
    return r


def task4():
    import copy
    n = 3
    m = 3
    matrix = generate_matrix(n, m, 9)
    b = generate_vector(n, 1)
    a = copy.deepcopy(matrix)
    for i in range(n):
        a[i].append(b[i])
    x = generate_vector(n, 0)
    n = len(a)
    m = len(a[0])
    for i in range(n):
        tmp = a[i][i]
        for j in range(i, m):
            if tmp != 0.0:
                a[i][j] /= tmp
        for j in range(i+1, n):
            tmp = a[j][i]
            for k in range(m-1, i-1, -1):
                a[j][k] -= tmp*a[i][k]
    x[n-1] = a[n-1][m-1]
    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1, n):
            x[i] -= a[i][j]*x[j]
    print_matrix(a)
    print(b)
    print(x)
    check(matrix, x, b)

def check(a, x, b):
    answer = multiply(a, x)
    print('answer', answer)
    print('right', b)


task4()

# In[ ]:

# Самостоятельная работа aka приближённый SVD
# Устное объяснение у доски

