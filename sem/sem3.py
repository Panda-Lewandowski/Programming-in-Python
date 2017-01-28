# This Python file uses the following encoding: utf-8
from math import sqrt
n = int(input('n = '))
p = []
mass_x = []
mass_y = []
for i in range(n):
    x, y = map(int, input(' x, y = ').split())
    mass_x.append(x)
    mass_y.append(y)

m_a_x = 0
min_x = 0
max_x = 0
min_y = 0
max_y = 0
for i in range(n):
    if (mass_y[i] > 0) and (m_a_x < sqrt(mass_x[i]**2 + mass_y[i]**2)):
        max_x, max_y = mass_x[i], mass_y[i]
        m_a_x = sqrt(mass_x[i]**2 + mass_y[i]**2)
m_i_n = sqrt(max_x**2 + max_y**2)
for i in range(n):
    if (mass_y[i] > 0) and (m_i_n > sqrt(mass_x[i]**2 + mass_y[i]**2)):
        min_x, min_y = mass_x[i], mass_y[i]
        m_i_n = sqrt(mass_x[i]**2 + mass_y[i]**2)
rast = sqrt((max_x - min_x)**2 + (max_y - min_y)**2)
print("""Наиболее удаленная точка с координатами [{0},{1}]
Наименее удаленная точка с координатами [{2},{3}]
Расстояние между точками {4:.3}""".format(max_x, max_y, min_x, min_y, rast))




