import sys
input = lambda: sys.stdin.readline().strip()

def fast_pow(a, b, p):
    res = 1
    a %= p
    while b > 0:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res        

def main():
    MOD = 100003
    m, n = map(int, input().split())

    total = fast_pow(m, n, MOD)
    safe = m % MOD * fast_pow(m - 1, n - 1, MOD) % MOD

    print((total - safe) % MOD)

main()
