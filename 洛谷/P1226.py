import sys
input = lambda: sys.stdin.readline().strip()

def main():
    a, b, p = map(int, input().split())
    result = 1
    pa = a;
    pb = b;
    a = a % p

    while b > 0:
        if b & 1:
            result = (result * a) % p
        a = (a * a) % p
        b >>= 1

    print(f'{pa}^{pb} mod {p}={result}')

main()