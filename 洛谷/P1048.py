import sys

def main():
    input = sys.stdin.readline
    T, M = map(int, input().split())

    dp = [0] * (T + 1) #背包空间

    for _ in range(M):
        w, v = map(int, input().split())
        for j in range(T, w-1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    print(dp[T])        


main()
