n = float(input())

if n >= 0 and n <= 25:
    print('Intervalo {}'.format('[0,25]'))
elif n > 25 and  n <= 50:
    print('Intervalo {}'.format('(25,50]'))  
elif n > 50 and n <= 75:
    print('Intervalo {}'.format('(50,75]'))       
elif n > 75 and n <= 100 :
    print('Intervalo {}'.format('(75,100]')) 
else:
    print('Fora de intervalo')    

