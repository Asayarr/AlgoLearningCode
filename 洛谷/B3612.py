n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1) 

m = int(input())
for i in range(len(a)):
    b[i+1] = (a[i] + b[i])

for _ in range(m):
    l, r = map(int,input().split())
    print(b[r] - b[l-1])
    