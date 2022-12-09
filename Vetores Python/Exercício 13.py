"""
13. Faça um programa que:
  - preencha um vetor com dez números reais
Calcule e mostre:
  - a quantidade de números negativos
  - a soma dos números positivos desse vetor
  - não use nenhuma função pronta da linguagem Python
"""
negativos = []
soma_positivos = 0
for i in range (10):
  valor = float(input('Insira um valor positivo ou negativo: '))
  if valor >= 0:
    soma_positivos += valor
  if valor < 0:
    negativos.append(valor)
print('Soma dos positivos:\n', soma_positivos)
print('Quantidade de negativos:\n', len(negativos))