n = int(input())
x = n -1
f = n

if 0 < n < 13:
    while x > 0:
        f *= x
        x -= 1
        
print(f)
        
