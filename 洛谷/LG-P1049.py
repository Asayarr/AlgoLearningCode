import sys

def main():
    input = sys.stdin.readline
    V = int(input())
    n = int(input())

    dp = [0] * (V + 1)
    
    for _ in range(n):
        w = v = int(input())
        for j in range(V, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    print(V - dp[V])

main()
