n = int(input())

if 5 < n < 2000:
    for i in range(1,n+1):
        if i % 2 == 0:
            p = i**2
            print(f'{i}^2 = {p}')
            

