import time
import random
import string
from math import sqrt


def partition(arr, l, h, key, sort):
    if key == 1:
        i = (l - 1)
        x = arr[h]

        for j in range(l, h):
            if arr[j] <= x:
                # increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1
    elif key == 2:
        i = (l - 1)
        x = arr[h][sort]
        for j in range(l, h):
            if arr[j][sort] <= x:
                # increment index of smaller element
                i += 1
                arr[i][sort], arr[j][sort] = arr[j][sort], arr[i][sort]

        arr[i + 1][sort], arr[h][sort] = arr[h][sort], arr[i + 1][sort]
        return i + 1


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def qsort(arr, l, h, key, sort):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h, key, sort)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


def sorting(el):
    a = list(range(1, el + 1))
    b = []
    for i in range(el, 0, -1):
        b.append(i)
    c = []
    for i in range(0, el):
        x = random.randint(0, 100)
        c.append(x)
    start = time.time()
    qsort(a, 0, el - 1, 1, sort=None)
    end1 = time.time() - start

    start = time.time()
    qsort(b, 0, el - 1, 1, sort=None)
    end2 = time.time() - start

    start = time.time()
    qsort(c, 0, el - 1, 1, sort=None)
    end3 = time.time() - start

    print('{0} элементов\t{1:^10.5f} {2:^10.5f} {3:^10.5f}'. \
          format(el, end1, end2, end3))


def password(n):
    a = string.ascii_lowercase + string.digits
    return ''.join([random.choice(a) for i in range(n)])


def card(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])


def access():
    a = ['A', 'B', 'C', 'D']
    return ''.join(random.choice(a))


def customers(el):
    cus = []
    for i in range(el):
        t = []
        c = card(10)
        t.append(c)
        k = password(6)
        t.append(k)
        x = random.randrange(1000, 5000)
        t.append(x)

        a = access()
        t.append(a)
        cus.append(t)
    return cus


print('НЕРЕКУРСИВНАЯ БЫСТРАЯ СОРТИРОВКА РАЗЛИЧНЫХ МАССИВОВ \n')
print('=' * 50)
print('Массивы:         Прямой     Обратный   Случайный')
print('=' * 50)

# sorting(100)
sorting(1000)
sorting(10000)
sorting(50000)
print('=' * 50)
print()

# num = list(map(int, input('Введите числа,которые хотите записать в таблицу: ').split()))
# print()
# qsort(num, 0, len(num) - 1)
# print('=' * 40)
# print('Число    Корень     Квадрат      2cc ')
# print('=' * 40)
# for j in range(len(num)):
#     print('{0:^5}    {1:<10.3f}  {2:<10.3f}  {3:<10}'.format(num[j], sqrt(num[j]),
#                                                           num[j] ** 2, bin(num[j]).replace('0b', '')))
# print('=' * 40)
#
n = 25
data = customers(n)
print('\nНЕСОРТИРОВАННЫЙ СПИСОК ЗАДОЛЖНИКОВ БАНКА\n')
print('=' * 75)
print('№ кредитной карты клиента    Пароль     Задолжность, руб   Уровень доступа')
print('=' * 75)
for j in range(len(data)):
    print(data[j][0], ' ' * 18, data[j][1], ' '*4, data[j][2], ' '*18, data[j][3])
q = int(input('''\nПо какому критерию хотите отсортировать список должников банка?
            0 - ПО НОМЕРУ КРЕДИТНОЙ КАРТЫ
            1 - ПО ПАРОЛЮ
            2 - ПО ЗАДОЛЖНОСТИ
            3 - ПО УРОВНЮ ДОСТУПА

Ваш выбор:  '''))
qsort(data, 0, n - 1, 2, q)
print('\nОТСОРТИРОВАННЫЙ СПИСОК ЗАДОЛЖНИКОВ БАНКА\n')
print('=' * 75)
print('№ кредитной карты клиента    Пароль     Задолжность, руб   Уровень доступа')
print('=' * 75)
for j in range(len(data)):
    print(data[j][0], ' ' * 18, data[j][1], ' '*4, data[j][2], ' '*18, data[j][3])
