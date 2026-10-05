import sys

def evaluate(s):
    total, sign, num = 0, 1, 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == ' ':
            pass
        elif ch == '+':
            total += sign * num
            sign, num = 1, 0
        elif ch == '-':
            total += sign * num
            sign, num = -1, 0
    total += sign * num
    return total

def solve():
    input = sys.stdin.readline
    n = int(input())

    def dfs(next, string):
        if next > n:
            if evaluate(string) == 0:
                print(string)
            return
        for op in ' +-':
            dfs(next + 1, string + op + str(next))

    dfs(2, "1")

solve()                           
    