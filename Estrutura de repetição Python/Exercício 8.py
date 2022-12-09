"""
8. Faça um algoritmo que calcule e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra (pode implementar com o comando while ou for):
 - Salário até 300, reajuste de 50%;
 - Salários maiores que 300, reajuste de 30%.
"""
i = 0
while i < 10:
  nome = input('Insira o nome do colaborador: ')
  salario = float(input(f'Insira  o salário do colaborador {nome}: '))
  if salario > 0 and salario <= 300:
    reajuste = salario * (50/100)
    salarior = salario + reajuste
    print (f'O salário do colaborador {nome} após o reajuste de 50% ficou em R$ {salarior:.2f}')
    i = i + 1
  elif salario > 300:
    reajuste = salario * (30/100)
    salarior = salario + reajuste
    print (f'O salário do colaborador {nome} após o reajuste de 30% ficou em R$ {salarior:.2f}')
    i = i + 1
  else:
    print('Você digitou um valor inválido!')
    i = i + 10