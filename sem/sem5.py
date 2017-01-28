n = 5
a = []
t = [1, 2, 3, 4, 5]
for i in range(n):
    a.append(t)
for i in range(n):
    for j in range(n):
        if i == j:
            a.remove(a[i][j])

