X = int(input())

if 1 <= X <= 1000:
    for i in range(X+1):
        if i % 2 == 1:
            print(i)

