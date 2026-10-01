import sys

def solve():
    input = sys.stdin.readline
    n , m = map(int, input().split())
    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().split())))

    seen = [[False] * m for _ in range(n)]
    ans = 0

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return
        if seen[x][y] or grid[x][y] != 1:
            return
        seen[x][y] = True
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(x + dx, y + dy)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not seen[i][j]:
                ans += 1
                dfs(i, j)
    print(ans)

solve()
        

