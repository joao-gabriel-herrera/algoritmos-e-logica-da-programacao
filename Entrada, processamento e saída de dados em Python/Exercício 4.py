"""
4. Faça um programa que:
 - receba salário de um funcionário
 - calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
"""
salario = float(input('Insira seu salário atual: '))
salarionovo = (salario + salario*(25/100))
print ('Seu salario novo é: ', salarionovo)