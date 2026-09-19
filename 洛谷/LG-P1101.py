n = int(input())
grid = [list(input()) for _ in range(n)]
mark = [[False] * n for _ in range(n)]

target = "yizhong"
dir= [(0, 1), (1, 1), (1, -1), (0, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)]

for i in range(n):
    for j in range(n):
        if grid[i][j] != "y":
            continue
        for x,y in dir:
            ok = True
            for k in range(len(target)):
                ni = i + x * k
                nj = j + y * k
                if not (0 <= ni < n and 0 <= nj < n):
                    ok = False
                    break
                if grid[ni][nj] != target[k]:
                    ok = False
                    break
            if ok:
                for k in range(len(target)):
                    ni = i + x * k
                    nj = j + y * k
                    mark[ni][nj] = True
        
for i in range(n):
    for j in range(n):
        if mark[i][j]:
            print(grid[i][j], end = '')
        else:
            print("*", end = '')
    print()  