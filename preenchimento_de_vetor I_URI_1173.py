n = 10*[0]

v = int(input())

for i in range(len(n)):  
    n[i] = v
    v = v * 2
    print(f'N[{i}] = {n[i]}')
    
