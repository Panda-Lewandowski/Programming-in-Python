# Найти окружность, проходящую хотя бы через три точки так,
# чтобы разность между количеством точек внутри окружности
#  и снаружи была минимальной
from math import sqrt, fabs


def input_points():
    t = 1
    mass = []
    print("""Точек должно быть больше 5-ти.
Введите координаты точек через пробел:
(для окончания ввода нажмите повторно enter)""")
    while t:
        t = list(map(int, input().split()))
        mass.append(t)
    mass.pop()  # удаление пустого списка в конце
    if len(mass) < 5:
        input_points()
    return mass


def distance_between_points(xy1, xy2):
    x_1 = xy1[0]
    x_2 = xy2[0]
    y_1 = xy1[1]
    y_2 = xy2[1]
    dis = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dis


def centre():
    global x_centre, y_centre
    ma = (y2 - y1) / (x2 - x1)  # наклонный коэф 1-ой хорды
    mb = (y3 - y2) / (x3 - x2)  # накл коэф 2-ой хорды
    if ma != mb:  # прямые совпадают
        x_centre = (ma * mb * (y1 - y3) + mb * (x1 + x2) - ma * (x2 + x3)) / (2 * (mb - ma))
        if ma == 0:
            y_centre = (-1 / mb) * (x_centre - (x2 + x3) / 2) + ((y2 + y3) / 2)
        else:
            y_centre = (-1 / ma) * (x_centre - (x1 + x2) / 2) + ((y1 + y2) / 2)


# решение через две хорды(окружность по трем точкам)
list_of_points = []
while len(list_of_points) < 5:
    list_of_points = input_points()
min_diff = None
min_radius = None
min_x = None
min_y = None
exit_code = 0
for i in range(len(list_of_points) - 3):  # первая связка-точка

    for j in range(i + 1, len(list_of_points) - 1):  # вторая связка-точка
        for k in range(j + 1, len(list_of_points)):  # третья связка-точка
            x1, y1 = list_of_points[i][0], list_of_points[i][1]
            x2, y2 = list_of_points[j][0], list_of_points[j][1]
            x3, y3 = list_of_points[k][0], list_of_points[k][1]
            points_outside = 0
            points_inside = 0
            if x1 == x2 == x3:  # три точки лежат на одной прямой
                break
            if x2 == x1:  # случай, когда одна хорда вертикальная, ее коэф = int
                x2, x3 = x3, x2
                y2, y3 = y3, y2
            elif x2 == x3:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            centre()
            radius = distance_between_points([x_centre, y_centre], [x1, y1])
            t1 = (x1 - x_centre) ** 2 + (y1 - y_centre) ** 2
            t2 = (x2 - x_centre) ** 2 + (y2 - y_centre) ** 2
            t3 = (x3 - x_centre) ** 2 + (y3 - y_centre) ** 2
            if (t1 == radius ** 2) and (t2 == radius ** 2) and (t3 == radius ** 2):
                for l in range(len(list_of_points)):
                    if l != i or l != j or l != k:
                        distance = distance_between_points([x_centre, y_centre], list_of_points[l])
                        if distance > radius:
                            points_outside += 1
                        elif distance < radius:
                            points_inside += 1
                if points_outside == points_inside:
                    print("""(Досрочно)Такая окружность найдена.
Координаты ее цетра: ({0:.3f},{1:.3f}).
Ее радиус равен: {2:.3f}""".format(x_centre, y_centre, radius))
                    exit_code = 1
                    break
                elif min_diff is None or fabs(points_outside - points_inside) < min_diff:
                    min_diff = fabs(points_outside - points_inside)
                    min_radius = radius
                    min_x = x_centre
                    min_y = y_centre
        if exit_code == 1:
            break
    if exit_code == 1:
        break
if exit_code != 1:
    print("""Такая окружность найдена.
Координаты ее цетра: ({0:.3f},{1:.3f}).
Ее радиус равен: {2:.3f}""".format(min_x, min_y, min_radius))

