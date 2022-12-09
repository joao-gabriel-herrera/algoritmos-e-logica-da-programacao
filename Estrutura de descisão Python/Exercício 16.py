# 16. Faça um programa que receba três números e mostre-os em ordem crescente. Suponha que o usuário digitará três números diferentes.

num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
num3 = float(input('Insira o terceiro valor: '))
if num1 < num2 and num1 < num3:
  if num2 < num3:
    print(f'A ordem crescente dos valores é: {num1:.2f}, {num2:.2f}, {num3:.2f}')
  else:
    print(f'A ordem crescente dos valores é: {num1:.2f}, {num3:.2f}, {num2:.2f}')
if num2 < num1 and num2 < num3:
  if num1 < num3:
    print(f'A ordem crescente dos valores é: {num2:.2f}, {num1:.2f}, {num3:.2f}')
  else:
    print(f'A ordem crescente dos valores é: {num2:.2f}, {num3:.2f}, {num1:.2f}')
if num3 < num1 and num3 < num2:
  if num2 < num1:
    print(f'A ordem crescente dos valores é: {num3:.2f}, {num2:.2f}, {num1:.2f}')
  else:
    print(f'A ordem crescente dos valores é: {num3:.2f}, {num1:.2f}, {num2:.2f}')