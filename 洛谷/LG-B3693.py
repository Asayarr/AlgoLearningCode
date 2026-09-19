import sys
T = int(input())
for _ in range(T):
    n , m , q = map(int, input().split())

    matrix = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)
        
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j] - arr[i][j] + matrix[i][j]

    ans = 0
    for _ in range(q):
        u, v, x, y = map(int, sys.stdin.readline().split())
        if x == u and y == v:
            temp = matrix[x - 1][y - 1]
        else:
            temp = arr[x][y] - arr[u-1][y] - arr[x][v-1] + arr[u-1][v-1]
        ans = ans ^ temp

    print(ans % (2 ** 64))