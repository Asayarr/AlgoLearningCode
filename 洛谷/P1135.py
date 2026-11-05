import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, a, b = map(int, input().split())
    data = list(map(int, input().split()))
    k = [0] * (n + 1)
    for i in range(1, n + 1):
       k[i] = data[i - 1]

    dist = [-1] * (n + 1)
    dist[a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            print(dist[x])
            return
        for nx in (x + k[x], x - k[x]):
            if 1 <= nx <= n and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    print(-1)

solve()            
       
