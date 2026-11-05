n = int(input())

first = [-1] * 7
last = [-1] * 7
first[0] = 0

s = 0
for i in range(1, n + 1):
    sid = int(input())
    s = (s + sid) % 7
    if first[s] == -1:
        first[s] = i
    last[s] = i

ans = 0
for r in range(7):
    if first[r] != -1:
        ans = max(ans, last[r] - first[r])

print(ans)