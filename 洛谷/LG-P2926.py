import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))

    MAX = max(a)
    bucket = [0] * (MAX + 1)
    for x in a:
        bucket[x] += 1

    need = [0] * (MAX + 1)
    for d in range(1, MAX + 1):
        if bucket[d]:
            for j in range(d, MAX + 1, d):
                need[j] += bucket[d]

    for x in a:
        print(need[x] - 1)

main()