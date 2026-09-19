T = int(input())           
for _ in range(T):
    N, p, q = input().split()
    p, q = int(p), int(q)
    num = int(N, p)
    if q == 2:    result = bin(num)[2:]
    elif q == 8:  result = oct(num)[2:]
    elif q == 10: result = str(num)
    else:         result = hex(num)[2:].upper()
    print(result)