# 5. Construir um algoritmo para calcular e apresentar a idade atual de algumas pessoas em relação ao ano atual, mas não é informado a quantidade de pessoas, então use como critério de parada (condição da estrutura de repetição, digitar zero no ano de nascimento para sair.

ano_atual = int(input('Insira o ano atual: '))
ano = int(input('Insira o ano de nascimento ou digite 0 para encerrar: '))
while ano > 0: 
 print(f'Sua idade atual é de {ano_atual - ano} anos.\n')
 ano = int(input('Insira o ano de nascimento ou digite 0 para encerrar: '))
print('Programa encerrado!')