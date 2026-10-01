import sys


def solve():
    input = sys.stdin.readline
    n, t = map(int, input().split())
    numbers = list(map(int, input().split()))

    ans = 0

    def dfs(i, total):
        nonlocal ans
        if i == n:                       # 每个数都做过"选/不选"决策了
            if total == t:
                ans += 1
            return

        # 分支1：选第 i 个数（超了就剪枝）
        if total + numbers[i] <= t:
            dfs(i + 1, total + numbers[i])

        # 分支2：不选第 i 个数
        dfs(i + 1, total)

    dfs(0, 0)
    print(ans)


solve()
