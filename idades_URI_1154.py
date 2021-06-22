total = 0
c = 0
idade = 1

while idade > 0:
    idade = int(input())
    if idade > 0:
        c += 1
        total += idade

media = total / c
print(f'{media:.2f}')
