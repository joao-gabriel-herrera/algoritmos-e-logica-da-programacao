# 5. Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input('Insira seu salário atual: '))
porcentagem = float(input('Insira a porcentagem do aumennto (Sem o símbolo!): '))
aumento = salario*(porcentagem/100)
salarionovo = salario + salario*(porcentagem/100)
print ('O valor do aumento foi de: ', aumento)
print ('Seu salario novo é: ', salarionovo)