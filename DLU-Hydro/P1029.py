import sys

def solve():
    data = sys.stdin.read().split()

    n = int(data[0])
    q = int(data[1])
    s = data[2]
    
    pre = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for c in range(26):
            pre[i][c] = pre[i - 1][c]
        
        ch = ord(s[i - 1]) - ord('a')
        pre[i][ch] += 1
        
    out = []
    idx = 3
    
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        
        max_cnt = 0
        for c in range(26):
            cnt = pre[r][c] - pre[l - 1][c]
            if cnt > max_cnt:
                max_cnt = cnt
                
        out.append(str(max_cnt))
        
    sys.stdout.write('\n'.join(out))

solve()