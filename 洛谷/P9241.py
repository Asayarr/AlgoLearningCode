import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        planes = []
        for _ in range(n):
            t, d, l = map(int, input().split())
            planes.append((t, d, l))
        used = [False] * n
            
        def dfs(cnt, cur):
            if cnt == n:
                return True
            for i in range(n):
                if used[i]:
                    continue
                T, D, L = planes[i]
                start = max(cur, T)
                if start > T + D:
                    continue
                used[i] = True
                if dfs(cnt + 1,start + L):
                    return True
                used[i] = False
            return False

        print("YES" if dfs(0, 0) else "NO")

solve()            
            
                    
                        
               
        
            



