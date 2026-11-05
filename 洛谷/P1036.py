import sys
from math import isqrt

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    def is_prime(x):
        if x < 2:
            return False
        for d in range(2, isqrt(x) + 1):
            if x % d == 0:
                return False
        return True    

    ans = 0
    def dfs(start, cnt, total):
        nonlocal ans
        if cnt == k:
            if is_prime(total):
                ans += 1
            return
        if n - start < k - cnt:
            return
        for i in range(start, n):
            dfs(i + 1, cnt + 1, total + arr[i])

    dfs(0, 0, 0)
    print(ans)

solve()
