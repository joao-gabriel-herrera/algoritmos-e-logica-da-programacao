"""
14. Faça um programa que:
  - receba dez números inteiros e armazene-os em um vetor
  - classifique os números em dois vetores, um com números pares e o outra com os ímpares
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
numeros =[]
pares = []
impares = []
for i in range (10):
  valor = int(input('Insira um valor: '))
  numeros.append(valor)
  if numeros[i] %2 == 0:
    pares.append(numeros[i])
  else:
    impares.append(numeros[i])
print('Pares:\n', pares)
print('Ímpares:\n', impares)