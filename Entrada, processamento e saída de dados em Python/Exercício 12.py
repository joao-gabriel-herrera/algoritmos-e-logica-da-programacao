# 12. Faça um programa que receba dois números, calcule e mostre um elevado ao outro. Use os caracteres **

num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))
resultado = num1 ** num2
print (f'O número {num1} elevado a {num2} é igual a: {resultado:.2f}')