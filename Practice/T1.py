import sys
def solve():
    input = sys.stdin.readline
    n = int(input())

    used = [False] * n
    path = []

    def dfs():
        if len(path) == n:
            print(*path)
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(i + 1)
            dfs()
            path.pop()
            used[i] = False

    dfs()        

solve()

        



