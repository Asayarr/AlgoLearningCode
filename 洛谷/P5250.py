import bisect
n = int(input())
woods = []

for _ in range(n):
    op, l =map(int,input().split())
    idx = bisect.bisect_left(woods, l)
    
    if op == 1:
        if idx < len(woods) and woods[idx] == l:
            print("Already Exist")
        else:
            woods.insert(idx, l)
            
    else:
        if not woods:
            print("Empty")
            continue
            
        left = woods[idx - 1] if idx > 0 else None
        right = woods[idx] if idx < len(woods) else None    
        
        if idx < len(woods) and woods[idx] == l:
            print(l)
            woods.pop(idx)   
        elif left is not None and right is not None:
            if l - left <= right - l:
                print(left)
                woods.pop(idx - 1)
            else:
                print(right)
                woods.pop(idx)          
        elif left is not None:
            print(left)
            woods.pop(idx - 1)
        else:
            print(right)
            woods.pop(idx)
