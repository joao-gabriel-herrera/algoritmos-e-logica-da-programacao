# 8. Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

num = int(input('Insira um valor inteiro: '))
if num % 2 == 0 :
  tipo = 'Par'
else:
  tipo = 'Ímpar'
if num < 0:
  valor = 'Negativo'
else:
  valor = 'Positivo'
print (f'O valor inserido é {tipo} e é um número {valor}. ')