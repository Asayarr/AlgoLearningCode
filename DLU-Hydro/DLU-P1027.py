t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    print(min(nums[2]-nums[1], nums[1]-nums[0]))

