# This Python file uses the following encoding: utf-8
r = []
l = None
input('Вводите элементы построчно, для прожолжения нажмите Enter, для завершения введите 0')
for i in range(12):
    l = int(input())
    if l == 0:
        break
    r.append(l)
if r:
    s = 0
    for i in range(len(r)):
        if r[i] > 0:
            s += r[i]
    if s == 0:
        print('Положительных элементов нет')
    else:
        r[1] = s
        print('Новый массив:  ', r)
else:
    print('Массив пуст')
