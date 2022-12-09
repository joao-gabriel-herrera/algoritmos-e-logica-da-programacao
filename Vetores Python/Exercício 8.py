# 8. Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores que receberão os elementos positivos e negativos e ao final apresente-os. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

numeros =[]
positivos = []
negativos = []
for i in range (10):
  valor = int(input('Insira um valor positivo ou negativo: '))
  numeros.append(valor)
  if numeros[i] >= 0:
    positivos.append(numeros[i])
  elif numeros[i] < 0:
    negativos.append(numeros[i])
print('Positivos:\n', positivos)
print('Negativos:\n', negativos)