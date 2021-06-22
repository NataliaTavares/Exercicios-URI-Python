A,B = input().split()

A,B = int(A),int(B)

multiplos = B % A
multiplos2 = A % B

if multiplos == 0 or multiplos2 == 0 :
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

