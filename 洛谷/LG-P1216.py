import sys

def main():
    input = sys.stdin.readline
    r = int(input())
    a = []
    for _ in range(r):
        a.append(list(map(int, input().split())))

    dp = a[-1][:]

    for i in range(r - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = a[i][j] + max(dp[j], dp[j + 1])

    print(dp[0])

main()           


