# DFS 回溯模板（4 合 1）
#
# 通用骨架：
#   def dfs(状态):
#       if 终止条件:
#           记录答案
#           return
#       for 每种选择:
#           if 不合法:
#               continue
#           做选择
#           dfs(新状态)
#           撤销选择


# ---------- 1. 全排列（顺序有关，用 used）----------
def permutations(a):
    n = len(a)
    used = [False] * n
    path = []
    res = []

    def dfs():
        if len(path) == n:
            res.append(path[:])
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(a[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


# ---------- 2. 组合（选 k 个，用 start）----------
def combinations(a, k):
    n = len(a)
    path = []
    res = []

    def dfs(start):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n):
            path.append(a[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res


# ---------- 3. 子集（每个元素 选 / 不选）----------
def subsets(a):
    n = len(a)
    path = []
    res = []

    def dfs(i):
        if i == n:
            res.append(path[:])
            return
        path.append(a[i])       # 选
        dfs(i + 1)
        path.pop()
        dfs(i + 1)              # 不选

    dfs(0)
    return res


# ---------- 4. 网格搜索（连通块，只标记不撤销）----------
def grid_dfs(grid, sx, sy):
    n, m = len(grid), len(grid[0])
    seen = [[False] * m for _ in range(n)]
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return
        if seen[x][y] or grid[x][y] != 1:
            return
        seen[x][y] = True
        for dx, dy in dirs:
            dfs(x + dx, y + dy)

    dfs(sx, sy)
    return seen


# 注意：
# 1. 前三种要撤销选择，网格搜索不用撤销
# 2. return False 要写在 for 循环外面
# 3. 剪枝放在递归之前
