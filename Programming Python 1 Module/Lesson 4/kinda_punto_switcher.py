# -*- coding: utf-8 -*-

import sys

rus = "йцукенгшщзхъфывапролджэячсмитьбю."
latin = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
for line in sys.stdin:
#for line in ['ghbdtn', 'привет']:
    for letter in line:
        index = latin.find(letter.lower())
        if index > -1 and index < len(rus):
            print(rus[index], end='')
        index = rus.find(letter.lower())
        if index > -1 and index < len(latin):
            print(latin[index], end='')
    print()
