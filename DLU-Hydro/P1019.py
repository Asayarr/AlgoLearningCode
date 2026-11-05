n, a, b = map(int, input().split())
print(0) if a + b < n else print(a + b - n)