# This Python file uses the following encoding: utf-8
x = []
N = int(input('Введите размерность матрицы: '))
for i in range(N):
    t = list(map(int, input('Введите новую строчку\t').split()))
    x.append(t)
print('Исходная матрица  ')
for i in range(N):
    for j in range(N):
        print('  ', x[i][j], sep=' ', end='')
    print()
print('Повернутая на 90 градусов против часовой стрелки  матрица   ')
for i in range(N - 1, -1, -1):
    for j in range(N):
        print('  ', x[j][i], sep=' ', end='')
    print()
