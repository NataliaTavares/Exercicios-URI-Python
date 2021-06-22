n = 1000*[0]

v = int(input())
x = 0

for i in range(len(n)):
    n[i] = x
    x += 1
    if x == v:
        x = 0
    print(f'N[{i}] = {n[i]}')    
