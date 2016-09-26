# -*- coding: utf-8 -*-

import sys

rus = "йцукенгшщзхъфывапролджэячсмитьбю."
latin = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
for line in sys.stdin:
    for letter in line:
        index = latin.find(letter.lower())
        print(letter, index, rus[index])


