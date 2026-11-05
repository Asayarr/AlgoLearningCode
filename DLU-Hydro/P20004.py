N, C = map(int, input().split())
nums = list(map(int, input().split()))

freq = {}
for v in nums:
    freq[v] = freq.get(v, 0) + 1

ans = 0
if C == 0:
    for v in freq:
        k = freq[v]
        ans += k * (k - 1)
else:
    for v in freq:
        if v + C in freq:
            ans += freq[v] * freq[v + C]

print(ans)