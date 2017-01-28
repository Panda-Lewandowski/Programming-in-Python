# This Python file uses the following encoding: utf-8
from math import fabs


def f(x):
    return x**2


def trap(a, b, n):   # Метод трапеций
    h = abs(b - a)/n
    s = (f(a) + f(b))/2
    for i in range(1, n):
        s += f(a + h * i)
    return s * h


def simpson38(a, b, n):   # Метод трёх восьмых(частный случай формулы Симпсона)
    h = abs(b - a)/(3 * n)
    m = 3 * n - 1
    s = f(a) + f(b)
    for i in range(1, m + 1):
        a += h
        if i % 3 == 0:
            s += 2 * f(a)
        else:
            s += 3 * f(a)
    return 3/8 * s * h



down = float(input('Введите нижнюю границу: '))
up = float(input('Введите верхнюю границу: '))
segments1 = int(input('Введите первое количество отрезков: '))
while segments1 % 3 != 0:
    print('Количество отрезков должно быть кратно трем! ')
    segments1 = int(input('Введите первое количество отрезков: '))
segments2 = int(input('Введите второе количество отрезков: '))
while segments2 % 3 != 0:
    print('Количество отрезков должно быть кратно трем! ')
    segments2 = int(input('Введите второе количество отрезков: '))


integral1_method1 = trap(down, up, segments1)
integral2_method1 = trap(down, up, segments2)
integral1_method2 = simpson38(down, up, segments1)
integral2_method2 = simpson38(down, up, segments2)


print('''\n\n

 ------------------------------------------------------------------
 Количество отрезков:        {0:<}                     {1:<}
 ------------------------------------------------------------------
 Метод трапеций              {2:<.7f}             {3:<.7f}
 ------------------------------------------------------------------
 Метод 3/8                   {4:<.7f}             {5:<.7f}
 ------------------------------------------------------------------

'''.format(segments1, segments2, integral1_method1, integral2_method1, integral1_method2, integral2_method2, ))

eps = float(input('\n\nВведите точность вычислений: '))
k = 1
while abs(trap(down, up, 2 * k) - trap(down, up, k)) > eps:
    k *= 2

print('\nЗначение интеграла с заданной точностью: {0:.7f}'.format(trap(down, up, k)))
print('Колическво участков при этом достигло: ', k)






