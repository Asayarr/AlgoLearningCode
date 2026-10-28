# 单调栈 / 单调队列模板
# 单调栈：找每个元素左右第一个更大/更小的元素
# 单调队列：滑动窗口最值

from collections import deque


# 单调栈：每个位置右边第一个更大的数，没有则 -1
def next_greater(a):
    n = len(a)
    res = [-1] * n
    stack = []                    # 存下标，对应值单调递减
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        res[i] = a[stack[-1]] if stack else -1
        stack.append(i)
    return res


# 单调栈：柱状图中最大的矩形面积（经典题）
def largest_rectangle(heights):
    stack = []                    # 存下标，对应高度单调递增
    ans = 0
    h = heights + [0]             # 末尾加 0，保证最后全部弹出
    for i, x in enumerate(h):
        while stack and h[stack[-1]] > x:
            height = h[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)
    return ans


# 单调队列：滑动窗口最大值
# 返回每个长度为 k 的窗口的最大值
def sliding_max(a, k):
    dq = deque()                  # 存下标，对应值单调递减
    out = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:        # 队头已经滑出窗口
            dq.popleft()
        if i >= k - 1:
            out.append(a[dq[0]])
    return out
