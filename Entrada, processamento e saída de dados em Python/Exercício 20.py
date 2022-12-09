"""
20. Faça um programa que receba um número real, encontre e mostre:
  - a parte inteira desse número;
  - a parte fracionária desse número;
  - o arredondamento desse número.
"""
numero = float(input('Insira o número: '))
pt_int = numero // 1
pt_fr = numero - pt_int
nr_arr = round (numero)
print (f'O valor da parte inteira é de: {pt_int:.2f}')
print (f'O valor da parte fracionária é de: {pt_fr:.2f}')
print (f'O número arredondado é: {nr_arr:.2f}')