
while True:
    try:
        n, m = input().split()
        n ,m = int(n), int(m)
        c = 0
        for x in range(n,m+1):
            if len(set(list(str(x)))) == len(str(x)):
                c += 1
        print(c)
                      
    except EOFError:
        break

    
