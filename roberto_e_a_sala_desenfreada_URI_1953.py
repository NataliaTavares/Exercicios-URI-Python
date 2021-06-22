while True:
    try:
        n = int(input())
        epr = 0
        ehd = 0
        intruso = 0

        if 1<=n<=100000:
            for i in range(n):
                a = input().lower()
                if 'epr' in a:
                    epr += 1
                elif 'ehd' in a:
                    ehd += 1
                else:
                    intruso += 1        

        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intruso}')
        
    except EOFError:
        break

