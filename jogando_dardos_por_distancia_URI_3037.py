maria = 0
joao = 0
pontos = 0

for i in range(int(input())):
    for o in range(3):
        a,b = input().split()
        a,b = int(a),int(b)
        pontos = a*b
        joao += pontos
    for o in range(3):
        a,b = input().split()
        a,b = int(a),int(b)
        pontos = a*b
        maria += pontos  
    if joao > maria:
        print(f'JOAO')
        maria = 0
        joao = 0
    else: 
        print(f'MARIA')
        maria = 0
        joao = 0





        


