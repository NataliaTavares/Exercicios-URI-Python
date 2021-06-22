nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas*15/100

print('TOTAL = R${:.2f}'.format(salario+comissao))

