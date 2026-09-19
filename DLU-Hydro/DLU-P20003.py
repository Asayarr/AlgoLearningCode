T = int(input())
for _ in range(T):
    n = int(input())
    p = str(input())
    q = ""
    for i in range(len(p)):
        q += chr(((ord(p[i]) - ord("A")) + n) % 26 + ord("A"))
    print(q)    