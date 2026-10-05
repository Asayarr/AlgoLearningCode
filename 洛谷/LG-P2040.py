import sys

def solve():
    input = sys.stdin.readline
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))

    ans = 99999
    def press(r, c):
        for dr, dc in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                grid[nr][nc] ^= 1

    def dfs(r, c, cnt):
        nonlocal ans
        if r == 3:
            if cnt < ans and all(grid[i][j] == 1 for i in range(3) for j in range(3)):
                ans = cnt
            return
        nr, nc = (r, c + 1) if c < 2 else (r + 1, 0)

        dfs(nr , nc, cnt)
        press(r, c)
        dfs(nr , nc, cnt + 1)
        press(r, c)

    dfs(0, 0, 0)
    print(ans)

solve()  