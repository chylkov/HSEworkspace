# Самостоятельная работа
# Постройте словарь (например, с помощью for),
# в котором для пар вещественных чисел x из [0, 1], y из [0, 1]
# с шагом сетки 0.1, будет записаны их расстояния Минковского до (0, 0)
# с любыми выбранными вами параметрами p, например,

# (0.0, 1.0) : (1.0, 1.0, 1.0)
# (в точке 0,1 расстояния до 0,0 по метрикам Минковского с параметрами p = 0.5, 1 и 2 равны единице)

# Распечатайте словарь. Как бы вы поменяли представление, чтобы было удобно распечатать значения "по сетке"?

mydict = {}
p_collection = [0.5, 1, 2]
grid = []
point = [0, 0]
step = 0.1
bound = 0.9

while point[0] < bound:
    while point[1] < bound:
        point[1] += step
        mydict[tuple(point)] = []

        for p in p_collection:
            el = (point[0] ** p + point[1] ** p) ** (1 / p)
            mydict[tuple(point)].append(el)

    point[0] += step
    point[1] = 0

for key, value in mydict.items():
    print(key, value)


# Самостоятельная работа
# Написать функцию, которая печатает (то есть без return)
# для заданных n_witches и step_witches
"""
1 little
2 little
...
step_witches little witches
step_witches+1 little
...

n_witches witches in the sky

То есть для КАЖДЫХ step_witches шагов писать не little, a little witches
А в конце -- witches in the sky.

Можно заводить дополнительные функции.
"""


def witches_song(n_witches, step_witches):
    for i in range(1, n_witches):
        if i % step_witches == 0:
            print(i, 'little witches')
        else:
            print(i, 'little')
    print(n_witches, 'witches in the sky')

witches_song(10, 3)


# Самостоятельная работа
# Функция с параметрами:
# - вектор(вектор =  список в нашем случае),
# - список векторов,
# - параметр-строка, задающий метрику: "l1" или "l2" (евклидова; и это значение по умолчанию)
# ФУНКЦИЯ возвращает ближайший к вектору-параметру вектор из списка-параметра (пусть вас не смущает полный перебор)

# Задать функцию, проверить, что она работает на простых примерах, и запустить на случайных векторах
# Подсказка: метрики тоже можно вычислять в отдельных функциях

import math


def l1(v1, v2):
    metric_value = 0
    for i in range(len(v1)):
        metric_value += math.fabs(v1[i] - v2[i])
    return metric_value


def l2(v1, v2):
    metric_value = 0
    for i in range(len(v1)):
        metric_value += (v1[i] - v2[i]) ** 2
    return math.sqrt(metric_value)


def the_closest_vector(main_vector, list_vector, metrics='l1'):
    metric_list = []

    for vector in list_vector:
        if metrics == 'l1':
            metric_list.append(l1(main_vector, vector))
        else:
            metric_list.append(l2(main_vector, vector))

    return list_vector[metric_list.index(min(metric_list))]


vectors = [[0, 0], [1, 1], [2, 2]]
main_v = [9, 9]
print(the_closest_vector(main_v, vectors, 'l2'))

# Самостоятельная работа: надо обязательно обернуть всю работу с матрицами в осмысленные функции!

# У вас есть матрица, скажем, размера 100500 x 100000, в память не поместится.
# Известно, что у неё очень мало ненулей

""" Не рекомендуется к запуску!

rows = 100500
cols = 100000
matrix_a = []
for row in range(rows):
    matrix_a.append([0] * cols)

"""

# 1) подумайте, как бы вы её представили с помощью словарей так, чтобы она уместилась в память,
#    и чтобы у вас был очень быстрый доступ к элементам по индексам, расскажите преподавателю
# 2) прочитайте матрицу A из файла, представив "новым" способом
# 3) транспонируйте её
# 4) запишите полученную матрицу B в новый файл
# 4.5) подумайте, как бы вы её представили так, чтобы вы могли эффективно
#     умножать такие матрицы друг на друга (с потерями в скорости доступа); хватит ли здесь одного представления?
# 5) запрограммируйте "умножение" A на B (в прежнем или новом виде) --
#    и проверьте корректность на каких-нибудь своих маленьких матрицах
# 6) запишите и AB в файл

def matrix_task():
    return NotImplemented