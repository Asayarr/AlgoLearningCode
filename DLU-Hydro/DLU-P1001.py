n = int(input())
activities = []
for _ in range(n):
    start, end = map(int, input().split())
    activities.append((end, start))  

activities.sort()

count = 0
last_end = -1

for end, start in activities:
    if start >= last_end:
        count += 1
        last_end = end

print(count)