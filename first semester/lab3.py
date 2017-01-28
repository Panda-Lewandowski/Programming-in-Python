# This Python file uses the following encoding: utf-8
from math import cos, log10, factorial
# y = (cos(x) * x * log10(x)) ** n / factorial(n + 1)

x = float(input('Введите значение х: '))
n = int(input('Введите начальное значение номера печати: '))
m = int(input('Введите рекомендуемое количество шагов: '))
hn = int(input('Введите шаг для печати: '))
eps = float(input('Введите E: '))


t = (cos(x) * x * log10(x)) ** n / factorial(n + 1)
s = round(t, 5)
print('\nНомер \tТекущая сумма ', sep='', end='')
# счетчик суммы до t меньшего е по модулю
while abs(t) >= eps:
    print('\n', n, '\t\t', round(s, 5), sep='', end='')
    n += hn
    t = (cos(x) * x * log10(x)) ** n / factorial(n + 1)
    s += t
# вывод окончательного значения
print('\n\nОкончательное значение суммы: ', '{0:.3f}'.format(s))
print('\nОкончательное количество шагов: ', n)

if n != m:
    print('\n\nРяд не сошелся за', m, 'рекомендуемых шагов')
else:
    print('\n\nРяд сошелся за', m, 'рекомендуемых шагов')
