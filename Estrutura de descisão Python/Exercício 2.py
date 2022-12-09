# 2. Faça um algoritmo que leia o nome e a idade de uma pessoa, verifique se a idade de uma pessoa é menor ou maior de idade. Considera-se maior de idade uma pessoa com 18 anos ou mais. Como saída o algoritmo deve informar o nome e a idade da pessoa e depois uma mensagem se ela é ou não maior de idade.

nome = input('Qual seu nome: ')
idade = int(input('Qual sua idade: '))
if idade < 18:
  print('Você é menor de idade!')
else:
  print ('Você é maior de idade!')