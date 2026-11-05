N = int(input())
a = list(map(int, input().split()))

def bubble_rounds(arr):
    n = len(arr)
    if n <= 1:
        return 1 if n == 1 else 0
    rounds = 0
    while True:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        rounds += 1
        if not swapped:
            break
    return rounds

pos = a.index(1)
ans = max(bubble_rounds(a[:pos]), bubble_rounds(a[pos + 1:]))

if ans == 0:
    print(1)
else:
    print(ans)