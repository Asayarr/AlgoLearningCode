# 最长上升子序列（LIS）模板


import bisect


# ---------- 1. O(n^2) DP ----------
def lis_n2(a):
    n = len(a)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# ---------- 2. O(n log n) 贪心 + 二分 ----------
def lis_nlogn(a):
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)       # 严格上升用 left
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# ---------- 3. 非严格上升 ----------
def lis_nonstrict(a):
    tails = []
    for x in a:
        i = bisect.bisect_right(tails, x)      # 非严格用 right
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# 注意：
# 1. 严格上升用 bisect_left，非严格上升用 bisect_right
# 2. O(n^2) 版答案是 max(dp)，不是 dp[n-1]
# 3. tails 不是 LIS 本身，但它的长度就是答案
