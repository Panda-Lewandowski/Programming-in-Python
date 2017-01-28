
# This Python file uses the following encoding: utf-8
from math import e

h = st_h = float(input('Введите начальное h:  '))
end_h = float(input('Введите конечное  h:  '))
step = float(input('Введите шаг:  '))
y1 = round(9.45 * (h ** 4) + 0.28 * h - 0.35, 4)
y2 = round((h - 1) ** 2 - 0.5 * (e ** h), 4)
y1max = y1
y2min = y2
y1min = y1
k = []  # список значений
t = []  # список аргументов
a = []  # список масштабированных значений
en = int(round((end_h-st_h)/step))

print("""
==================================================
      Y1         Y2              H             N
==================================================""")
for n in range(1, en + 2):
    k.append(y1)
    t.append(round(h, 2))
    if h > end_h:
        break
    if abs(y1) < 10000 or abs(y2) < 10000:
        print('{0:^7.3f}      {1:^7.3f}      {2:^.2f}       {3:^2d}'.format(y1, y2, h, n))
    else:
        print('{0:<7.3e}      {1:<7.3e}      {2:^10.2f}       {3:<2d}'.format(y1, y2, h, n))
    y1 = round(9.45 * (h ** 4) + 0.28 * h - 0.35, 4)
    y2 = round((h - 1) ** 2 - 0.5 * (e ** h), 4)
    h += step
    if y1 >= y1max:
        y1max = y1
    if y2 <= y2min:
        y2min = y2
    if y1 <= y1min:
        y1min = y1


print('__________________________________________________')

q = y2min / y1max
print('\n\nОтношение мин. у2 к макс. у1 равно: ', round(q, 4))

print('\n\nГрафик функции Y1\n')


for i in range(len(k)):
    m = round((k[i] - y1min) / (y1max - y1min) * 75)
    a.append(m)  # местоположение точки в масштабе

nol = round((- y1min) / (y1max - y1min) * 75)  # координата нулевой линии
print('-' * 75 + '> Y  H')

for i in range(len(a)):
    c = []
    if 0 <= nol <= 75:
        if a[i] < nol:
            c.append(' ' * a[i] + '*' + ' ' * (nol - a[i] - 1) + '|' + ' ' * (76 - nol + 1))
        elif a[i] == nol:
            c.append(' ' * a[i] + '*' + ' ' * (76 - a[i] + 1))
        elif a[i] > nol:
            c.append(' ' * nol + '|' + ' ' * (a[i] - nol - 1) + '*' + ' ' * (76 - a[i] + 1))
    else:
        c.append(' ' * (a[i] - 1) + '*' + ' ' * (76 - a[i] - 1))
    for j in range(len(c)):
        print(c[j], end='')
    if i % 2 != 0:
        print(' ', t[i], sep='', end='')
    print()
if 0 <= nol <= 75:
    print(' ' * nol + 'V X')
