n, k, q = map(int, input().split())
MAX = 200000

diff = [0] * (MAX + 2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

cnt = [0] * (MAX + 2)
for i in range(1, MAX + 1):
    cnt[i] = cnt[i - 1] + diff[i]

pref = [0] * (MAX + 2)
for i in range(1, MAX + 1):
    pref[i] = pref[i - 1] + (1 if cnt[i] >= k else 0)

for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])