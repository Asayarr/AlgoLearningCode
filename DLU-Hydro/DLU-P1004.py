n, q = map(int, input().split())
a = list(map(int, input().split()))

counts = [0] * (n + 1)
for i in range(1 , n + 1):
    counts[i] = counts[i - 1] + a[i - 1] #0 1 3 6 9 14

for _ in range(q):
    L, R = map(int, input().split())
    print(counts[R] -counts[L - 1])