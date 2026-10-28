# 背包模板


# ---------- 1. 01 背包（每个物品最多一次）----------
def knapsack01(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        w, v = weights[i], values[i]
        for j in range(W, w - 1, -1):          # 倒序
            if dp[j - w] + v > dp[j]:
                dp[j] = dp[j - w] + v
    return dp[W]


# ---------- 2. 完全背包（每个物品无限次）----------
def knapsack_complete(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        w, v = weights[i], values[i]
        for j in range(w, W + 1):              # 正序
            if dp[j - w] + v > dp[j]:
                dp[j] = dp[j - w] + v
    return dp[W]


# ---------- 3. 01 背包计数（方案数）----------
def knapsack_count(items, M):
    """items 是每个物品的重量，求恰好装满 M 的方案数"""
    dp = [0] * (M + 1)
    dp[0] = 1                                  # 空方案算 1 种
    for x in items:
        for j in range(M, x - 1, -1):          # 倒序
            dp[j] += dp[j - x]
    return dp[M]


# ---------- 4. 二维版（好懂，用来理解）----------
def knapsack01_2d(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(W + 1):
            dp[i][j] = dp[i - 1][j]            # 不拿
            if j >= w:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)   # 拿
    return dp[n][W]


# 注意：
# 1. 01 背包倒序，完全背包正序，写反就错
# 2. 计数型：dp[j] += dp[j-w]，dp[0] = 1
# 3. dp 数组开 W+1
