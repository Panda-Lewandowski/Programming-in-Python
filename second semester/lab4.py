# написать функцию для нахождения седловой точки
# целочисленной прямоугольной матрицы
# матрица (9,8)
# седловая точка - мин в столбце и мах в строке


def saddle_point():
    global b
    no_code = 0
    for i in range(1, len(b) - 1):
        t = max(b[i])
        ind = b[i].index(t)
        mint = None
        if ind != 0 and ind != (len(b[i]) + 1):
            for j in range(len(b)):
                if mint is None or b[j][ind] < mint:
                    mint = b[j][ind]
                    x, y = j, ind
        if t == mint:
            print('Седловая точка матрицы: ', t, '    (', x, '-ая строка, ', y, '-ый столбец)')
            no_code = 1
    if no_code == 0:
        print('Седловых точек нет')


def input_matrix():
    global b
    m = int(input('Введите количество строк(не больше 9): '))
    n = int(input('Введите количество столбцов(не больше 8): '))
    if m > 9 or n > 8:
        input_matrix()
    else:
        for i in range(m):
            t = list(map(int, input('Введите новую строчку\t').split()))
            b.append(t)
        print('\nИсходная матрица  ')
        for i in range(m):
            for j in range(n):
                print('  ', b[i][j], sep=' ', end='')
            print()


b = []
input_matrix()
saddle_point()

