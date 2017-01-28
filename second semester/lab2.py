from math import log as ln


def input_vector(cols):
    # Введение вектора
    massive = list(map(int, input('Введите вектор Z (не больше {0} элементов):\t'.format(cols)).split()))
    return massive


def form_matrix(massive, rows, cols, matrix):
    global max_ind, min_ind
    print('Сформированная матрица: ')
    y = 0.05
    """if ln((rows + 1) * 0.05) < 0:
        min_sum = (min(massive) * ln((rows + 1) * 0.05)) * cols
        max_sum = -min_sum
    else:
        min_sum = (max(massive) * ln((rows + 1) * 0.05)) * cols
        max_sum = -min_sum
    print(max_sum, min_sum)"""
    min_sum = None
    max_sum = None
    for i in range(rows):
        y += 0.05
        s = 0
        list_of_row = []  # список-строка
        for j in range(cols):
            t = massive[j] * ln(y)
            list_of_row.append(t)
            s += t
            print('{0:.3f}\t'.format(t), end='')
        print()
        matrix.append(list_of_row)
        if max_sum is None or s > max_sum:
            max_sum = s
            max_ind = i
        if min_sum is None or s < min_sum:
            min_sum = s
            min_ind = i


def form_vector(cols, matrix):
    print('Сформированный вектор:')
    for i in range(cols * 2):
        if i < cols:
            t = matrix[max_ind][i]
            print('{0:.3f}\t'.format(t), end='')
        else:
            t = matrix[min_ind][i - cols]
            print('{0:.3f}\t'.format(t), end='')


K = 100
M = 100
while K >= 10 and M >= 12:
    K = int(input('Введите количество столбцов матрицы (не больше 10):\t'))
    M = int(input('Введите количество строк матрицы (не больше 12):\t'))
    max_ind = None
    min_ind = None
    if K <= 10 and M <= 12:
        F = []
        Z = input_vector(K)
        form_matrix(Z, M, K, F)
        form_vector(K, F)
    else:
        print('Неверные значения. Повторите ввод.\n')
