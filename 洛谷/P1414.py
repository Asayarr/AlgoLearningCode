import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    MAX = max(a)

    bucket = [0] * (MAX + 1)
    for x in a:
        bucket[x] += 1

    count = [0] * (MAX + 1)
    for d in range(1, MAX + 1):
        count[d] = sum(bucket[d::d])  #gcd为d时 有几个

    ans = [0] * (n + 1) #ans下标为第k个，ans[c]为选个的时候的gcd是多少
    for d in range(1, MAX + 1):
        c = count[d]
        if c > 0 and d > ans[c]:
            ans[c] = d

    for k in range(n-1, 0, -1):
        if ans[k + 1] > ans[k]:
            ans[k] = ans[k + 1] #例如10 25 5 选3个的最大公约数为5，那么选2个最大公约数一定要大于等于5，若不是就是出现了10 10 10这样的情况，会导致ans为 0 0 10

    print('\n'.join(map(str, ans[1:])))
    
main()