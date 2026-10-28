import sys
input = lambda: sys.stdin.readline().strip()

def main():
    return

main()


# 1. 一行多个整数
#    n, m = map(int, input().split())
#
# 2. 读 n 行，每行两个数
#    pairs = []
#    for _ in range(n):
#        x, y = map(int, input().split())
#        pairs.append((x, y))
#
# 3. 多组数据
#    T = int(input())
#    for _ in range(T):
#        n = int(input())
#        a = list(map(int, input().split()))
#
# ============================================================
# 输出写法
# ============================================================
#
# 1. 只有一个答案
#    print(ans)
#
# 2. 多组数据，每组一行（先攒后印）
#    out = []
#    for _ in range(T):
#        out.append(str(答案))
#    sys.stdout.write('\n'.join(out) + '\n')
#
# 3. 一行输出多个数，用空格隔开
#    print(' '.join(map(str, ans)))

