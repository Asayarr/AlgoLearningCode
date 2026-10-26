import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * (M + 1)
    dp[0] = 1


    for x in a:
        for j in range(M, x - 1, -1):
            dp[j] += dp[j - x]

    print(dp[M])

main()

