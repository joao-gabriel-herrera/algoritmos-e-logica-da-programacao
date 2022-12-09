"""
12. Faça um programa que:
  - preencha um vetor com quinze elementos inteiros
  - verifique a existência de elementos iguais a 30, mostrando os índices/posições em que apareceram.
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
numeros = []
for i in range (15):
  numeros.append(int(input('Insira um valor: ')))
for i in range (len(numeros)):
  if numeros[i] == 30:
   print(f'O número 30 foi identificado na {i+1}º posição')
