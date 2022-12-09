# 12. Faça um programa que receba a idade e a altura de 20 pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos.

pessoas = 0
altura_cont = 0
banco_altura = 0
while pessoas < 20:
  idade = int(input('Insira sua idade: '))
  altura = float(input('Insira sua altura: '))
  if idade >= 20:
    banco_altura = banco_altura + altura
    altura_cont = altura_cont + 1
  pessoas = pessoas + 1
media = banco_altura / altura_cont
print(f'A média de altura das pessoas acima de 20 anos é de {media:.2f}')