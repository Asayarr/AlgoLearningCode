n = int(input())
s, b = [], []

for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

ans = float('inf')
def dfs(i, sour, bitter, cnt):
    global ans
    if i == n:
        if cnt > 0:
            ans = min(ans, abs(sour - bitter))
        return
    dfs(i + 1, sour * s[i], bitter + b[i], cnt + 1)
    dfs(i + 1, sour, bitter, cnt)

dfs(0, 1, 0, 0)
print(ans)