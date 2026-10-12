import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    col = [False] * n
    d1 = [False] * (2 * n)
    d2 = [False] * (2 * n)
    pos = [0] * n
    count = 0
    out = []

    def dfs(r):
        nonlocal count
        if r == n:
            count += 1
            if count <= 3:
                out.append(' '.join(str(pos[i] + 1) for i in range(n)))
            return
        for c in range(n):
            if col[c] or d1[r - c + n] or d2[r + c]:
                continue
            col[c] = d1[r - c + n] = d2[r + c] = True
            pos[r] = c
            dfs(r + 1)
            col[c] = d1[r - c + n] = d2[r + c] = False
    dfs(0)
    out.append(str(count))
    for line in out:
        print(line)

main()