# 15. Faça um programa que receba dois números e mostre o maior.

num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
if num1 > num2:
  print (f'{num1} é maior que {num2}')
elif num2 > num1:
  print (f'{num2} é maior que {num1}')
else:
  print('Os dois valores são iguais!')