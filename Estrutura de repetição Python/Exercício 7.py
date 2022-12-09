# 7. Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares. Pode implementar com o comando while ou for.

i = 0
par = 0
impar = 0
while i < 23:
  num = int(input('Insira o número: '))
  if num % 2 == 0:
    par = par + 1
  else:
    impar = impar + 1
  i = i + 1
print(f'\n')
print(f'Você tem {par} números pares e {impar} números ímpares.')