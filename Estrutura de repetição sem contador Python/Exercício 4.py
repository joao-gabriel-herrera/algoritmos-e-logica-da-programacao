# 4. Faça um programa que receba a idade e a altura de várias pessoas. Calcule e exiba a média das alturas das pessoas com mais de 20 anos. Para encerrar a entrada de dados, digite uma idade negativa ou igual a zero.

print(f'Para encerrar o programa digite uma idade menor ou igual a 0. \n')
idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura: '))
pessoas = 0
alturas = 0
while idade > 0:
 if idade > 20:
   pessoas = pessoas + 1
   alturas = alturas + altura     
 idade = int(input('Insira sua idade: '))
 if idade == 0 or idade < 0:
   break
 altura = float(input('Insira sua altura: '))
print(f'A média de alturas das pessoas que tem mais de 20 anos ({pessoas} pessoas) é de {alturas/pessoas :.2f}')