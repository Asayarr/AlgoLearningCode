# 前缀和 / 差分模板


# ---------- 一维前缀和 ----------
def build_prefix(a):
    n = len(a)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    return pref


def range_sum(pref, l, r):
    """区间 [l, r] 的和，闭区间，0-indexed"""
    return pref[r + 1] - pref[l]


# ---------- 二维前缀和 ----------
def build_prefix_2d(a, n, m):
    pref = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            pref[i+1][j+1] = pref[i][j+1] + pref[i+1][j] - pref[i][j] + a[i][j]
    return pref


def rect_sum(pref, r1, c1, r2, c2):
    """矩形 (r1,c1) 到 (r2,c2) 的和，闭区间"""
    return pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]


# ---------- 差分 ----------
def build_diff(n):
    return [0] * (n + 2)


def add_range(diff, l, r, v):
    """区间 [l, r] 每个元素加 v"""
    diff[l] += v
    diff[r + 1] -= v


def restore_diff(diff, n):
    """对 diff 做前缀和，还原出每个位置的值"""
    res = [0] * n
    cur = 0
    for i in range(n):
        cur += diff[i]
        res[i] = cur
    return res


# 注意：
# 1. 前缀和数组长度是 n+1，下标 0 存 0
# 2. 二维前缀和建表时用容斥：左 + 上 - 左上 + 当前
# 3. 差分数组长度至少 n+1，因为会访问 diff[r+1]
