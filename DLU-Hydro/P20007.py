T = int(input())
pair = {')': '(', ']': '[', '}': '{'}

for _ in range(T):
    s = input()
    stack = []
    ok = True
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif stack == [] or stack[-1] != pair[ch]:
            ok = False
        else:
            stack.pop()
            
    if stack:
        ok = False
    print("YES" if ok else "NO")