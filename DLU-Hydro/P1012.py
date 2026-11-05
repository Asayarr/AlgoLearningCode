m, n = map(int, input().split())

a = [[0] * n for _ in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(n):
        a[i][j] = temp[j]

b = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        b[i][j] = a[m - j - 1][i]

for row in b:
    print(*row)