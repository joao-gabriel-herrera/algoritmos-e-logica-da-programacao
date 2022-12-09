# 1.a) Faça um algoritmo que calcule e exiba o salário reajustado de um funcionário de acordo com a seguinte regra: Salário até 500, reajuste de 50%.

salario = float(input('Insira seu salário: '))
if salario >= 500:
   salario = (salario - salario * (50/100))
   print (f'O salario com reajuste será de R$ {salario:.2f}')
else:
   print (f'Seu salário não sofrerá reajuste, sendo assim ele se mantém em R$ {salario:.2f}')