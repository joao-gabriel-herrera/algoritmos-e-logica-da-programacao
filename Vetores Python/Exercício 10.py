"""
10. Faça um programa que:
  - preencha um vetor com seis elementos numéricos inteiros.
Calcule e mostre:
  - todos os números pares;
  - a quantidade de números pares;
  - todos os números ímpares;
  - a quantidade de números ímpares
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
numeros =[]
pares = []
impares = []
for i in range (5):
  valor = int(input('Insira um valor: '))
  numeros.append(valor)
  if numeros[i] %2 == 0:
    pares.append(numeros[i])
  else:
    impares.append(numeros[i])
print(f'Existem {len(pares)} números pares, sendo eles:\n {pares}')
print(f'Existem {len(impares)} números ímpares sendo eles:\n {impares}')