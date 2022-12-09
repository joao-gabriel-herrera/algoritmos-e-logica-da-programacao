"""
6. Faça um programa que receba um conjunto de valores inteiros, calcule e exiba o maior e o menor valor do conjunto.
 - Para encerrar a entrada de dados, deve ser digitado o valor zero;
 - Para valores negativos, deve ser enviada uma mensagem;
 - Esses valores (zero e negativos) não entrarão na lógica de encontrar o maior e o menor valor.
"""
num = int(input('Insira um valor ou digite 0 para encerrar a coleta de dados: '))
maior = num
menor = num
while num != 0:
   if num < 0:
    print('Valor negativo inserido!')
   elif num > maior:
    maior = num
   elif num < menor:
    menor = num 
   num = int(input('Insira um valor ou digite 0 para encerrar a coleta de dados: '))
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')