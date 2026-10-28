# BFS 模板


from collections import deque


# ---------- 1. 网格最短路（边权相同）----------
def bfs_shortest(grid, sx, sy, tx, ty):
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    dist[sx][sy] = 0
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        if x == tx and y == ty:
            return dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return -1


# ---------- 2. 洪水填充 / 连通块 ----------
def flood_fill(grid, sx, sy):
    n, m = len(grid), len(grid[0])
    target = grid[sx][sy]                  # 要填充的值（不一定是 1）
    seen = [[False] * m for _ in range(n)]
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    q = deque([(sx, sy)])
    seen[sx][sy] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not seen[nx][ny] and grid[nx][ny] == target:
                    seen[nx][ny] = True
                    q.append((nx, ny))
    return cnt


# ---------- 3. 一维 BFS（楼层、状态转移等）----------
def bfs_1d(start, target, neighbors):
    """neighbors(x) 返回 x 能走到的下一层节点"""
    dist = {start: 0}
    q = deque([start])
    while q:
        x = q.popleft()
        if x == target:
            return dist[x]
        for nx in neighbors(x):
            if nx not in dist:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return -1


# 注意：
# 1. 入队时就标记，不要等出队才标记
# 2. 用 deque.popleft()，不要用 list.pop(0)
# 3. 先判断越界，再访问数组
