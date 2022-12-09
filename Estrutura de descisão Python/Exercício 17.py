# 17. Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

print('Insira 3 valores em ordem crescente:')
num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
num3 = float(input('Insira o terceiro valor: '))
print('insira um valor aleatório:')
num4 = float(input('Insira o valor aleatório: '))
if num4 > num3:
  print(f'a ordem decrescente dos valores digitados é de: {num4:.2f}, {num3:.2f}, {num2:.2f}, {num1:.2f}')
elif num4 > num2 and num4 < num3:
  print(f'a ordem decrescente dos valores digitados é de: {num3:.2f}, {num4:.2f}, {num2:.2f}, {num1:.2f}')
elif num4 > num1 and num4 < num2:
  print(f'a ordem decrescente dos valores digitados é de: {num4:.2f}, {num3:.2f}, {num2:.2f}, {num1:.2f}')
elif num4 < num1:
  print(f'a ordem decrescente dos valores digitados é de: {num3:.2f}, {num2:.2f}, {num1:.2f}, {num4:.2f}')