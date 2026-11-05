import sys
from math import gcd

input = lambda: sys.stdin.readline().strip()

def main():
    x, y = map(int, input().split())
    num = x * y
    count = 0
    for i in range(x, y + 1, x):
        if num % i == 0 and gcd(num // i, i) == x:
            count += 1

    print(count)

main()
