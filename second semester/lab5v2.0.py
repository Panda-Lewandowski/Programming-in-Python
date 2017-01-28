# улучшенный комбинированный
from math import sin, cos, pi, ceil
import matplotlib.pyplot as plt
import numpy as np


def f(x, key):
    if key == 1:
        return x ** 2 - 1
    if key == 0:
        return sin(x) * x
    if key == 2:
        return x ** 2 + 1
    if key == 3:
        return -x ** 2 + 3
    if key == 4:
        return sin(x) + x * cos(x)
    if key == 5:
        return 2 * cos(x) - x * sin(x)


def derivative_of_f(x, key):
    if key == 1:
        return 2 * x
    if key == 0:
        return sin(x) + x * cos(x)
    if key == 4:
        return 2 * cos(x) - x * sin(x)
    if key == 5:
        return -3 * sin(x) - x * cos(x)


def input_data():
    global a, b, h, eps_x, eps_y, max_n
    print('Введите:')
    a, b = map(float, input('- начало и конец отрезка: ').split())
    h = float(input('- шаг: '))
    eps_x = float(input('- точность по х: '))
    eps_y = float(input('- точность по y: '))
    max_n = int(input('- максимальное число итераций: '))


def task(key):
    global list_of_roots, intersection, flag, bend, ext

    left = a
    right = a + h
    t = 0

    res = []
    no_roots = True
    q = None
    for i in range(ceil(abs(a - b) / h)):
        if (f(left, key) >= 0 and f(right, key) <= 0) or (f(left, key) <= 0 and f(right, key) >= 0):
            if right <= b:
                res = finding_root(left, right, key)
            elif right >= b:
                res = finding_root(left, b, key)
            if res:

                no_roots = False

                t += 1
                if res[2] == '-':
                    print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t        {3}\t       {4}  {5:>5.0f}  {6:>10.0f}'. \
                          format(t, res[0], res[1], res[2], res[3], res[4], res[5]))
                    print('-' * 69)
                elif q is None or res[2] != q:
                    if key == 1:
                        intersection.append(res[2])
                        print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t{3:>10.6f}\t{4:>8.0e}  {5:>5.0f}  {6:>10.0f}'. \
                              format(t, res[0], res[1], res[2], f(res[2], 2), res[4], res[5]))
                    if key == 5:
                        bend.append(res[2])
                        print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t{3:>10.6f}\t{4:>8.0e}  {5:>5.0f}  {6:>10.0f}'. \
                              format(t, res[0], res[1], res[2], f(res[2], 0), res[4], res[5]))
                    if key == 4:
                        ext.append(res[2])
                        print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t{3:>10.6f}\t{4:>8.0e}  {5:>5.0f}  {6:>10.0f}'. \
                              format(t, res[0], res[1], res[2], f(res[2], 0), res[4], res[5]))
                    elif key == 0:
                        list_of_roots.append(res[2])
                        print('{0:<2.0f}  {1:>5.2f}\t{2:>5.2f}\t{3:>10.6f}\t{4:>8.0e}  {5:>5.0f}  {6:>10.0f}'. \
                              format(t, res[0], res[1], res[2], res[3], res[4], res[5]))
                    print('-' * 69)
            q = res[2]
        left = right
        right += h
    if no_roots:
        print('Корней на заданном промежутке нет.')


def finding_root(v, w, key):
    global eps_x, eps_y, max_n, flag
    n = 1
    error_code = 0
    x_chord = v
    x_tan = w
    if f(v, key) == 0:
        if key == 1:
            key += 1
        return v, w, v, f(v, key), n, error_code
    elif f(w, key) == 0:
        if key == 1:
            key += 1
        return v, w, w, f(w, key), n, error_code
    else:
        try:
            while abs(x_chord - x_tan) >= eps_x or abs(x_chord - x_tan) >= eps_y:
                if n > max_n:
                    error_code = 1
                x_chord -= f(x_chord, key) / derivative_of_f(x_chord, key)
                x_tan -= (f(x_tan, key) * (x_chord - x_tan)) / (f(x_chord, key) - f(x_tan, key))
                n += 1
        except ZeroDivisionError:
            flag = 1
            error_code = 3
            return v, w, '-', '-', n, error_code
    if error_code == 1:
        if key == 1:
            key += 1
        flag = 1
        return v, w, '-', '-', n, error_code
    elif abs(f(x_chord, key)) > abs(f(x_tan, key)):
        if v <= x_tan <= w:
            if key == 1:
                key += 1
            return v, w, x_tan, f(x_tan, key), n, error_code
        else:
            error_code = 2
            flag = 1
            return v, w, '-', '-', n, error_code
    elif abs(f(x_tan, key)) > abs(f(x_chord, key)):
        if v <= x_chord <= w:
            if key == 1:
                key += 1
            return v, w, x_chord, f(x_chord, key), n, error_code
        else:
            error_code = 2
            flag = 1
            return v, w, '-', '-', n, error_code


def plotting1(key):
    global list_of_roots
    m = np.linspace(a, b, 1000)
    y = []
    z = []
    u = []
    for k in range(len(m)):
        y.append(f(m[k], key))
        z.append(f(m[k], 4))
        u.append(f(m[k], 5))
    for k in range(len(list_of_roots)):
        if k == 0:
            plt.scatter(list_of_roots[k], f(list_of_roots[k], key), marker='o', color='r', label='Roots')
        else:
            plt.scatter(list_of_roots[k], f(list_of_roots[k], key), marker='o', color='r')
    for k in range(len(ext)):
        if k == 0:
            plt.scatter(ext[k], f(ext[k], 0), marker='s', color='m', label='Extrema')
        else:
            plt.scatter(ext[k], f(ext[k], 0), marker='s', color='m')
    for k in range(len(bend)):
        if k == 0:
            plt.scatter(bend[k], f(bend[k], 0), marker='p', color='orange', label='Inflection')
        else:
            plt.scatter(bend[k], f(bend[k], 0), marker='p', color='orange')
    plt.plot(m, y, color='k', linewidth=1.0, label='x*sin(x) ')
    plt.plot(m, z, color='g', alpha=0.5, linewidth=1.0, label='The first derivative')
    plt.plot(m, u, color='pink', alpha=0.5, linewidth=1.0, label='The second derivative')
    plt.grid(True, color='b', linewidth=0.5)
    plt.axis([a, b, -15., 15.])
    plt.ylabel('f(x)', size=14)
    plt.xlabel('x', size=14)
    plt.legend(frameon=False)
    plt.title('The function, its the first and the second \nderivatives with points of inflection and extrema')
    plt.show()


def plotting2(key):
    q = np.linspace(intersection[0], intersection[1], 100)
    m = np.linspace(-10, 10, 100)
    y1 = []
    r1 = []
    y2 = []
    r2 = []
    for k in range(len(m)):
        y1.append(f(m[k], key))
        key += 1
        r1.append(f(m[k], key))
        key -= 1
    print(key)
    plt.plot(m, y1, color='k', linewidth=1.0, label='f(x)=x^2+1')
    plt.plot(m, r1, color='m', linewidth=1.0, label='g(x)=-x^2-3')
    for k in range(len(q)):
        y2.append(f(q[k], key))
        key += 1
        r2.append(f(q[k], key))
        key -= 1

    plt.grid(True, color='b', linewidth=0.5)
    for k in range(len(intersection)):
        if k == 0:
            plt.scatter(intersection[k], f(intersection[k], key), marker='o', color='r', label='Intersection')
        else:
            plt.scatter(intersection[k], f(intersection[k], key), marker='o', color='r')
    plt.axis([intersection[0] - 2, intersection[1] + 2, -5., 5.])
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.fill_between(q, y2, r2, color='pink', alpha=0.5, label='Integral')
    plt.title('Illustration of finding the square \nwith the help of the integral')
    plt.legend(frameon=False)
    plt.show()


def trap(down, up, n, key):  # Метод трапеций
    height = abs(up - down) / n
    s = (f(down, key) + f(up, key)) / 2
    for i in range(1, n):
        s += f(down + height * i, key)
    return s * height


print('\nНАХОЖДЕНИЕ КОРНЕЙ ОДНОЙ ФУНКЦИИ:')
input_data()
print("""\n

=====================================================================
#     А            В       х               f(x)  Итераций Код ошибки
=====================================================================
""")
list_of_roots = []
intersection = []
bend = []
ext = []
task(0)
print('\nТочки экстремумов\n')
task(4)
print('\nТочки перегиба\n')
task(5)
plotting1(0)

print('\nНАХОЖДЕНИЕ ПЛОЩАДИ ФИГУРЫ, ЗАКЛЮЧЕННОЙ МЕЖДУ ДВУМЯ ФУНКЦИЯМИ:')
input_data()
print("""\n
=====================================================================
#     А            В       точки пересечения  g(x)  Итераций Код ошибки
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
error_str = """Коды ошибок:
  0 - ошибок нет
  1 - Превышено количество итераций
  2 - Выход корня за границы отрезка(данный метод не приминим)
  3 - Деление на ноль"""
print(error_str)
