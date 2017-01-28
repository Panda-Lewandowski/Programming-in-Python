# This Python file uses the following encoding: utf-8
from math import sqrt

b = []
l = None
input('Вводите элементы построчно, для прожолжения нажмите Enter,для выхода введите 0')
for i in range(10):
    l = int(input())
    if l == 0:
        break
    b.append(l)

if b:
    b_min = min(b)
    if b_min < 0:
        print('Минимальный элемент отрицательный ')
    else:
        c = []
        x = None
        for i in range(len(b)):
            x = b[i] / sqrt(b_min)
            c.append(round(x, 5))
        print('Новый массив: ', c)
else:
    print('Массив пуст')
