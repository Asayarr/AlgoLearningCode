def has9(n):
    return '9' in str(n)

numbers = [9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

t = int(input())
for _ in range(t):
    x = int(input())
    i = 0
    a = numbers[i]
    found = False
    while a <= x // 2:
        if has9(x - a):
            print(a, x - a)
            found = True
            break
        i += 1
        a = numbers[i]
    if not found:
        print(-1)