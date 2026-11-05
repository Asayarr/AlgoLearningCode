T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    freq = {}
    for v in nums:
        freq[v] = freq.get(v, 0) + 1
        if freq[v] > N // 2:
            print(v)
            break