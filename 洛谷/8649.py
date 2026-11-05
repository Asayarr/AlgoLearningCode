n, k = map(int, input().split())
cnt = [0] * k
cnt[0] = 1

s = 0
for _ in range(n):
    s = (s + int(input())) % k
    cnt[s] += 1

ans = 0
for c in cnt:
    ans += c * (c - 1) // 2

print(ans)