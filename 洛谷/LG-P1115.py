import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    cur = a[0]
    best = a[0]

    for i in range(1, n):
        cur = max(a[i], a[i] + cur)
        best = max(best, cur)
    print(best)

main()