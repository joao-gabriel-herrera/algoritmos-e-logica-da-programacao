# 7. Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de 50,00 sobre o salário base e paga imposto que deve ser lido e é aplicado sobre o salário base.

salariob = float(input('Insira o seu salário: ' )) 
imposto = float(input('Insira o percentual do imposto (Sem o símbolo!) ' ))
salariofinal = salariob + 50 - (salariob * imposto/100)
print ('Seu salário com os devidos descontos e bônus é: ', salariofinal)