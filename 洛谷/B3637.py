import sys
import bisect

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    tails = []

    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x

    print(len(tails))

main()