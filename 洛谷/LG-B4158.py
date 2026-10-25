import sys
from math import isqrt

def build_primes(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(n) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i in range(2, n + 1) if is_p[i]]            

p_list = build_primes(4000)

def is_prime(x):
    if x < 2:
        return False
    for p in p_list:
        if p * p > x:
            break
        if x % p == 0:
            return False
    return True
    
def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        s = input().strip()
        length = len(s)
        best = -1

        def dfs(i, val):
            nonlocal best
            if best != -1:
                return
            if i == length:
                if is_prime(val):
                    best = val
                return
            if s[i] == '*':
                for j in range(10):
                    dfs(i + 1, val * 10 + j)
                    if best != -1:
                        return
            else:
                dfs(i + 1, val * 10 + int(s[i]))

        dfs(0 ,0)
        print(best)
                 
main()