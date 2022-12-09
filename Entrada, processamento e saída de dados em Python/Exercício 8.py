# 8. Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento de um mês.

deposito = float(input('Digite valor do depósito: '))
taxa = float(input('Digite a taxa de juros: '))
rendimento = deposito + (deposito * taxa/100)
print ('Seu dinheiro com o rendimento é: ', rendimento)