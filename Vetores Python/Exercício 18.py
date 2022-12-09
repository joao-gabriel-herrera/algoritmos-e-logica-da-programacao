"""
18. Faça um programa que:
  - leia um vetor de 10 números inteiros
  - exiba na tela os números positivos e seus respectivos índices.
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
numeros =[]
for i in range (5):
  numeros.append(int(input('Insira um valor positivo ou negativo: ')))
for i in range(len(numeros)):
  if numeros[i] >= 0:
    print(f'O numero que está na {i+1}ª posição (nº{numeros[i]}) é positivo')