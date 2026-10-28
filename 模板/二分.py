# 二分模板
# 前提：数组有序
# 关键区别：
#   精确查找：while lo <= hi，找到就返回
#   找边界 / 二分答案：while lo < hi，用 mid 压缩区间


def lower_bound(a, x):
    """第一个 >= x 的位置"""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(a, x):
    """第一个 > x 的位置"""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def binary_search(a, x):
    """精确查找，找到返回下标，找不到返回 -1"""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_answer_min(lo, hi, check):
    """求最小的满足 check 的值
    check 必须单调：false ... false true ... true
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def binary_answer_max(lo, hi, check):
    """求最大的满足 check 的值
    check 必须单调：true ... true false ... false
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2      # 注意这里要 +1，否则死循环
        if check(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


# 注意：
# 1. lower_bound / upper_bound 的 hi 取 len(a)，不是 len(a)-1
# 2. 二分答案求最大值时，mid 要写 (lo + hi + 1) // 2
# 3. 精确查找用 while lo <= hi，找边界用 while lo < hi，混用会死循环
