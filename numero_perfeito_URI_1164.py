n = int(input())
c = 1
p = 0

for i in range(n):
    x = int(input())
    while c < x:
        if x % c == 0:
            p += c
        c += 1
    if p == x:
        print(f'{x} eh perfeito')
        c = 1 
        p = 0   
    else:
        print(f'{x} nao eh perfeito')
        c = 1  
        p = 0  

