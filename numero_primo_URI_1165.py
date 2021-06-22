n = int(input())
c = 0

for i in range(1,n+1):
    p = int(input())
    for x in range(1,p+1):
        if p % x == 0:
            c += 1
    if c == 2:
        print(f'{p} eh primo')
        c =  0
    else:        
        print(f'{p} nao eh primo')
        c =  0

        
