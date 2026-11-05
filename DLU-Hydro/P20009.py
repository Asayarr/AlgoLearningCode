T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    slow = 0
    for fast in range(n):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    print(*nums)