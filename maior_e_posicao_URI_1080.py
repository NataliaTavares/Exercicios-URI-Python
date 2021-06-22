x = 0
maior = 0

for i in range(0,100):
    x = int(input())
    if x > maior:
        maior = x  
        posicao = i + 1

print(maior)
print(posicao)
    

