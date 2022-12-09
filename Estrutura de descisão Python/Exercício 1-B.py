# 1.b) Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 500, reajuste de 50%; Salários maiores que 500, reajuste de 30%.

salario = float(input('Insira seu salário: '))
if salario <= 500:
   salario = (salario - salario * (50/100))
   print (f'O salario com reajuste será de R$ {salario:.2f}')
else:
   salario = (salario - salario * (30/100))
   print (f'O salario com reajuste será de R$ {salario:.2f}')