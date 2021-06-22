x = 10*[0]
c = 0

while c < 10:
    x[c] = int(input())
    if x[c] <= 0:
        x[c] = 1
    c += 1    

for i in range(0,c):
    print(f'X[{i}] = {x[i]}')

