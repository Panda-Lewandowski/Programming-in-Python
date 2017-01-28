# This Python file uses the following encoding: utf-8
x = []
p = []
for i in range(7):
    t = list(map(float, input('Введите новую строчку  ').split()))
    if len(t) > 10:
        print('Строчка не должна содержать более 10 элементов ')
        t = list(map(float, input('Введите новую строчку  ').split()))
        p.append(t)
    else:
        p.append(t)


for i in range(len(p)):
    for j in range(len(p[i])):
        if p[i][j] > 0:
          x.append(p[i][j])
x.sort()
if not x:
    print('В матрице нет положительных элементов')
else:
    print('Матрица  ')
    for i in range(len(p)):
        for j in range(len(p[i])):
            print('  ', p[i][j], sep=' ', end='')
        print()
    print()
    print('Сформированный вектор  ')
    for i in range(len(x)):
        print('  ', x[i], sep='  ', end='')
