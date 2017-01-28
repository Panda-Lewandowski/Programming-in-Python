# This Python file uses the following encoding: utf-8
p = []
n = int(input('Введите размерность матрицы: '))
for i in range(n):
    t = list(map(str, input('Введите новую строчку  ').split()))
    if len(t) > n:
        print('Строчка не должна содержать более N элементов ')
        t = list(map(float, input('Введите новую строчку  ').split()))
        p.append(t)
    else:
        p.append(t)

for i in range(len(p)):
        for j in range(len(p[i])):
            print('  ', p[i][j], sep=' ', end='')
        print()

word = str(input('Введите слово: '))

_str_ = ''
buf = []
for i in range(n):
    for j in range(n):
        _str_ += p[i][j]
    buf.append(_str_)
    _str_ = ''
for i in range(n):
    entry = buf[i].find(word)
    if entry != -1:
        print('Слово начинается в {0} строке в {1} столбце и располагается горизонтально'.format(i + 1, entry + 1))

_str_ = ''
buf = []
for i in range(n):
    for j in range(n):
        _str_ += p[j][i]
    buf.append(_str_)
    _str_ = ''

for i in range(n):
    entry = buf[i].find(word)
    if entry != -1:
        print('Слово начинается в {0} столбце в {1} строке и располагается вертикально'.format(i + 1, entry + 1))


            





