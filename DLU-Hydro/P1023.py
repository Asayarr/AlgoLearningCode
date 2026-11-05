t = int(input())
for _ in range(t):
    n = input()
    buckets = [0] * 10
    for i in n:
        buckets[int(i)] += 1
    times = 0
    res = 1
    index = len(buckets) - 1
    while times < 2:
        if buckets[index] > 0:
            buckets[index] -= 1
            times += 1
            res *= index
        else:
            index -= 1
    print(res)