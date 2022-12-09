# 9. Criar um algoritmo que leia dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. Obs.: percentual = quantidade contada * 100 / quantidade total. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

numeros = []
soma_numeros = 0
menor = 0
maior = 0
pares = 0
for i in range (5):
  numeros.append(int(input(f'Insira o {i+1}º valor: ')))
  soma_numeros += numeros[i]
  if len(numeros) == 1:
    maior = numeros[i]
    menor = numeros[i]
  if numeros[i] > maior:
    maior = numeros[i]
  elif numeros[i] < menor:
    menor = numeros[i]
for i in range (len(numeros)):
  if numeros[i] % 2 == 0:
    pares += 1
media = soma_numeros / len(numeros)
percentual = pares * 100 / len(numeros)
print('-'*21)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A média dos valores é de: {media:.2f}')
print(f'O percentual de números pares é de: {percentual:.2f}%')
