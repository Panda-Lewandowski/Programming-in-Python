# This Python file uses the following encoding: utf-8
# объединение множеств
a = list('concert')
b = list('concept')
c = a + b
new = []
for i in range(len(c)):
    if c[i] not in new:
        new.append(c[i])
print(new)
