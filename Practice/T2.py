import sys

def solve():
    input = sys.stdin.readline
    n , t = map(int, (input().split()))
    numbers = list(map(int, (input().split())))
    ans = 0

    def dfs(total, start):
        nonlocal ans
        if total == t:
            ans += 1    
        for i in range(start, n):
            if total + numbers[i] > t:
                continue
            dfs(total + numbers[i], i + 1)

    dfs(0, 0)
    print(ans)

solve()

