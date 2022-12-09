"""
19. Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário, número 1 para a escolha da soma, ou número 2 para a raiz quadrada, também receba os dados necessários para executar cada operação.

Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.
"""
print(f'Menu de operações:\n')
print('1 - Somar dois números')
print(f'2 - Raiz quadrada do número\n')
I = int(input('Escolha a opção desejada: '))
if I == 1:
  num1 = float(input('Insira o 1º valor: '))
  num2 = float(input('Insira o 2º valor: '))
  print (f'A soma de {num1:.2f} + {num2:.2f} = {num1 + num2:.2f}')
if I == 2:
  num = float(input('Insira o valor para ver sua raiz quadrada: '))
  print (f'A raiz de {num:.2f} é: {num**(1/2)}')