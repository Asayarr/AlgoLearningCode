n = int(input())
a = list(map(int, input().split()))

pos = {}
for i in range(len(a)):
    v = a[i]
    pos[v] = i + 1

Q = int(input())
for _ in range(Q):
    m = int(input())
    print(pos.get(m, 0))