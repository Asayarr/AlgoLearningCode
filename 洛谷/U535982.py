T = int(input())
for _ in range(T):
    n = int(input())
    string = input()
    odd, even= 0 , 0
    for i in range(0, 2 * n, 2):
        if string[i] == "A":
            odd += 1
    for i in range(1, 2 * n, 2):
        if string[i] == "A":
            even += 1
    print(min(odd, even))    