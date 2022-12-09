# 6. Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

salariob = float(input('Insira seu salário atual: '))
salariog = salariob + (salariob * 5/100)
salarioi = salariog - (salariob * 7/100)
print ('Seu salario com respectivos descontos e bônus é: ', salarioi)