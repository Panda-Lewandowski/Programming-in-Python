# This Python file uses the following encoding: utf-8
#  упорядочить массив по возрастанию
L = [1, 3, 5, 8, 14, 23, 37]
r = int(input('r = '))
for i in range(len(L)):
    if L[i] < r < L[i + 1]:
        part1 = L[:i + 1]
        part2 = L[i + 1:]
part1.append(r)
L = part1 + part2
print(L)
