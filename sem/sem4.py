n = 5
r = []
for i in range(n):
    r.append([0] * n)

for i in range(n):
    for j in range(n):
        r[i][j] = abs(i - j) + 1
        if i > j:
            r[i][j] = 0

for i in range(n):
    print(r[i])
