# метод улучшенный комбинированный
# -9 5 3
from math import sin, cos, pi, ceil
import matplotlib.pyplot as plt
import numpy as np


def f(x, key):
    if key == 1:
        return x ** 2 - 1
    if key == 0:
        return sin(x)
    if key == 2:
        return x ** 2 + 1
    if key == 3:
        return -x ** 2 + 3


def derivative_of_f(x, key):
    if key == 1:
        return 2 * x
    if key == 0:
        return cos(x)


def input_data():
    global a, b, h, eps_x, eps_y, max_n
    print('Введите:')
    a, b = map(float, input('- начало и конец отрезка: ').split())
    h = float(input('- шаг: '))
    eps_x = float(input('- точность по х: '))
    eps_y = float(input('- точность по y: '))
    max_n = int(input('- максимальное число итераций: '))


def task(key):
    global list_of_roots, intersection, flag
    list_of_roots = []
    intersection = []
    p = a
    t = 0
    q = None
    error_str = """Коды ошибок:
    0 - ошибок нет
    1 - Превышено количество итераций
    2 - Выход корня за границы отрезка(данный метод не приминим)
    3 - Деление на ноль"""
    res = []
    no_roots = True
    try:
        for i in range(ceil(abs(a - b) / h)):
            res = None
            if p + h >= b:
                if (f(p, key) <= 0 >= f(b, key)) or (f(p, key) >= 0 <= f(b, key)):
                    res = finding_root(p, b, key)
            else:
                if (f(p, key) <= 0 >= f(p + h, key)) or (f(p, key) >= 0 <= f(p + h, key)):
                    res = finding_root(p, p + h, key)

            if res:
                print(res)
                no_roots = False
                if key == 1:
                    intersection.append(res[2])
                t += 1
                if res[2] == '-':
                    print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t        {3}\t       {4}  {5:>5.0f}  {6:>10.0f}'. \
                          format(t, res[0], res[1], res[2], res[3], res[4], res[5]))
                    print('-' * 69)
                else:
                    print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t{3:>10.6f}\t{4:>8.0e}  {5:>5.0f}  {6:>10.0f}'. \
                          format(t, res[0], res[1], res[2], res[3], res[4], res[5]))
                    print('-' * 69)
            p += h
    except ZeroDivisionError:
        flag = 1
        print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t        {3}\t      {4}  {5}  {6:>10.0f}'. \
              format(t, p, p + h, '-', '-', '-', 3))
        print('-' * 69)
    if no_roots:
        print('Корней на заданном промежутке нет.')
    print(error_str)


def finding_root(v, w, key):
    global eps_x, eps_y, max_n, list_of_roots, flag
    n = 1
    error_code = 0
    x_chord = v
    x_tan = w
    if f(v, key) == 0:
        list_of_roots.append(v)
        if key == 1:
            key += 1
        return v, w, v, f(v, key), n, error_code
    elif f(w, key) == 0:
        list_of_roots.append(w)
        if key == 1:
            key += 1
        return v, w, w, f(w, key), n, error_code
    else:
        while abs(x_chord - x_tan) >= eps_x or abs(x_chord - x_tan) >= eps_y:
            x_chord -= f(x_chord, key) / derivative_of_f(x_chord, key)
            x_tan -= (f(x_tan, key) * (x_chord - x_tan)) / (f(x_chord, key) - f(x_tan, key))
            n += 1
    if n > max_n:
        error_code = 1
    if error_code == 1:
        if key == 1:
            key += 1
        flag = 1
        return v, w, '-', '-', n, error_code
    elif abs(f(x_chord, key)) > abs(f(x_tan, key)):
        if v <= x_tan <= w:
            list_of_roots.append(x_tan)
            if key == 1:
                key += 1
            return v, w, x_tan, f(x_tan, key), n, error_code
        else:
            error_code = 2
            return v, w, '-', '-', n, error_code
    elif abs(f(x_tan, key)) > abs(f(x_chord, key)):
        if v <= x_chord <= w:
            list_of_roots.append(x_chord)
            if key == 1:
                key += 1
            return v, w, x_chord, f(x_chord, key), n, error_code
        else:
            error_code = 2
            return v, w, '-', '-', n, error_code


def plotting1(key):
    global list_of_roots
    m = np.linspace(a, b, 1000)
    y = []
    plt.subplot(2, 1, 1)
    for k in range(len(m)):
        y.append(f(m[k], key))
    plt.plot(m, y, color='b', linewidth=2.0)
    for k in range(len(list_of_roots)):
        plt.scatter(list_of_roots[k], f(list_of_roots[k], key), marker='o', color='r')
    plt.grid(True, color='b', linewidth=0.5)
    plt.axis([a, b, -10., 10.])
    plt.ylabel('y', size=14)
    plt.title('The roots of equation at a predetermined interval')

    r = np.linspace(-8 * pi, 8 * pi, 1000)
    z = []
    for k in range(len(r)):
        z.append(f(r[k], key))
    plt.subplot(2, 1, 2)
    plt.plot(r, z, color='g', linewidth=2.0)
    plt.grid(True, linewidth=0.5)
    plt.axis([-8 * pi, 8 * pi, -5., 5.])
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.title('Function')
    plt.show()


def plotting2(key):
    q = np.linspace(intersection[0], intersection[1], 100)
    m = np.linspace(-10, 10, 100)
    y = []
    r = []
    for k in range(len(m)):
        y.append(f(m[k], key))
    plt.plot(m, y, color='g', linewidth=2.0)
    key += 1
    for k in range(len(m)):
        r.append(f(m[k], key))
    plt.plot(m, r, color='k', linewidth=2.0)
    plt.grid(True, color='b', linewidth=0.5)
    for k in range(len(intersection)):
        plt.scatter(intersection[k], f(intersection[k], key), marker='o', color='r')
    plt.axis([intersection[0] - 2, intersection[1] + 2, -5., 5.])
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    # plt.fill_between(m, y, r, color='m')
    plt.show()


def trap(down, up, n, key):  # Метод трапеций
    height = abs(up - down) / n
    s = (f(down, key) + f(up, key)) / 2
    for i in range(1, n):
        s += f(down + height * i, key)
    return s * height


print('\nНАХОЖДЕНИЕ КОРНЕЙ ОДНОЙ ФУНКЦИИ:')
input_data()
print("""\n____________________________________________________________
        ______________________________________
       |          Функция                     |
       | 0 = sin(x)                           |
       |          Производная                 |
       | f'(x) = cos(x)                       |
       |______________________________________|

=====================================================================
#     А            В       х               f(x)  Итераций Код ошибки
=====================================================================
""")
task(0)
plotting1(0)
print('\nНАХОЖДЕНИЕ ПЛОЩАДИ ФИГУРЫ, ЗАКЛЮЧЕННОЙ МЕЖДУ ДВУМЯ ФУНКЦИЯМИ:')
input_data()
print("""\n____________________________________________________________
        ______________________________________
       | Функция            Производная       |
       | g1(x) = x^2 + 1    g1'(x)= 2x        |
       |                                      |
       | g2(x) = -x^2 + 3   g2'(x)= -2x       |
       |______________________________________|

=====================================================================
#     А            В       точки пересечени  g(x)  Итераций Код ошибки
=====================================================================
""")
flag = 0
task(1)
if flag == 0:
    area1 = trap(intersection[0], intersection[1], 1000, 2)
    area2 = trap(intersection[0], intersection[1], 1000, 3)
    square = abs(area1 - area2)
    print('Площадь фигуры равна: {0:2.4f}'.format(square))
    plotting2(2)
else:
    print('Площадь найти нельзя, см. код ошибки')
