"""
14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
  - a idade atual da pessoa;
  - quantos anos ela terá em 2050.
"""
anon = int(input('Insira o ano de nascimento: '))
anoatual = int(input('Digite o ano em que estamos: '))
idadef = 2050 - anon
idadeatual = anoatual - anon
print ('Hoje você tem' ,idadeatual,'anos e em 2050 você terá',idadef,'anos.')