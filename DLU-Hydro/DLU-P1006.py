a, b= map(int, input().split())

if a < b:
    a , b = b , a

while(a%b != 0):
    temp = b
    b = a % b
    a = temp
    
print(b)