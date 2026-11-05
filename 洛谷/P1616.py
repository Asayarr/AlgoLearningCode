import sys

def main():
    input = sys.stdin.readline
    t, m = map(int, input().split())

    dp = [0] * (t + 1)
    
    for _ in range(m):
        w, v = map(int, input().split())
        for j in range(w, t + 1):
            dp[j] = max(dp[j], dp[j-w] + v)

    print(dp[t])

main()
