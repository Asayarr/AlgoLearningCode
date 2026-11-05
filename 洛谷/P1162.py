import sys
from collections import deque

def solve():
       input = sys.stdin.readline
       n = int(input())
       grid = [[0] * (n + 2)]
       for _ in range(n):
            row = list(map(int, input().split()))
            grid.append([0] + row + [0])
       grid.append([0] * (n + 2))

       q = deque()
       q.append((0, 0))
       grid[0][0] = -1
       while q:
             x, y = q.popleft()
             for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1)):
                   nx, ny = x + dx, y + dy
                   if 0 <= nx < n+2 and 0 <= ny < n+2 and grid[nx][ny] == 0:
                         grid[nx][ny] = -1
                         q.append((nx,ny))
       out = []                  
       for i in range(1, n + 1):
             line = []
             for j in range(1, n + 1):
                   if grid[i][j] == -1:
                         line.append("0")
                   elif grid[i][j] == 0:
                         line.append("2")
                   else:
                         line.append("1")
             out.append(" ".join(line))
       print("\n".join(out))

solve()