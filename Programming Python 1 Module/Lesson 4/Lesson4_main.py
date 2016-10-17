# In[20]:

"""
Самостоятельная работа
Дана строка, постройте "перевёрнутую строку"
Пример: abcd -> dcba
"""
def f1():
    # s = "И у облаков -- вокал Боуи"
    s = 'а р о з а у п а л а н а л а п у а з о р а'
    inverse_string = ''
    for i in range(len(s)-1, -1, -1):
        inverse_string += s[i]
    print(inverse_string)


# In[26]:

"""
Самостоятельная работа
Дана строка s, построить список строк из пар подряд идущих символов s [не внахлёст]
Пример: "abcsd" -> ["ab", "cs", "d"]
"""
def f2():
    s = "Биликопытапели"
    answer = []
    step = 0
    for i in range(2, len(s)+1, 2):
        print(i)
        answer.append(s[step:i])
        step = i
    print(answer)

"""
Самостоятельная работа "метод нарезок".
Создать текстовый файл, наполнить чем угодно.

Разбить на n равных по количеству строк частей.
Случайным образом перемешать (см. ниже), склеить и записать в новый файл.
"""
def f3():
    import random
    import copy
    n = 5
    indices = list(range(n))
    random.shuffle(indices)

    texts = []
    inputfile = open("ex1.txt", "r")
    all_lines = inputfile.readlines()
    patch_capacity = len(all_lines) // n
    print('capacity', patch_capacity)
    current = 0
    cur_t = []
    index_last = 0

    for line in all_lines:
        if current < patch_capacity:
            cur_t.append(line)
            current +=1
        else:
            texts.append(copy.deepcopy(cur_t))
            cur_t = [line]
            current = 1

    if len(cur_t) > 0:
        texts.append(cur_t)
    with open("filefile.txt", "w") as of:
        for i in indices:
            for line in texts[i]:
                of.write(line)
            of.write('')


    print(indices)


# In[56]:

"""
Самостоятельная работа: kinda punto switcher
Создать питоновский файл, написать в него программу,
которая в вечном цикле (for something in sys.stdin)
ждёт очередного текста из стандартного ввода и выводит
его в латинской раскладке.
"""
# done in another file


"""
Самостоятельная работа: brackets pretty printer
Тоже файл с вечным циклом. На вход подают т.н. правильную
скобочную последовательность (нет нарушений во вложенности скобок
вроде ")())") -- и в одну строчку.

Мы распечатываем "красиво" (ну как "красиво"):
1) каждая скобка с новой строки,
2) открывающаяся увеличивает отступ,
3) закрывающаяся -- уменьшает.

Пример: ()(()()) ->
(
)
(
    (
    )
    (
    )
)
"""
def f4():
    input = "()(()())"
    indent = 0
    last = input[0]
    print('(')
    for i in range(1, len(input)-1):
        if input[i] == '(' and last == input [i]:
            indent += 1
        if input[i] == ')' and last == input [i]:
            indent -= 1
        print(' ' * indent * 4 + input[i])
        last = input[i]
    print(input[len(input) - 1])

f4()
"""
*Самостоятельная работа
Проверить правильность скобочной последовательности
"""
# already done in Algorithms&Structures/21-09-2016/brackets.py
