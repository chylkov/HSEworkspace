
# coding: utf-8

# In[11]:

print("Hello Jupyter Notebook!")


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

def task4():
    n = 2
    m = [[1, 2], [3, 4]]
    b = [5, 11]



# In[ ]:

# Самостоятельная работа aka приближённый SVD
# Устное объяснение у доски

