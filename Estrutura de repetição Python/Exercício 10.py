# 10. Faça um algoritmo que calcule e informe a média de idades de 5 alunos. Pode implementar com o comando while ou for.

alunos = 0
idadefinal = 0
while alunos < 5:
  idade= int(input('Insira sua idade: '))
  idadefinal= idadefinal + idade
  alunos = alunos + 1
print (f'\n\n')
idaderesultado = idadefinal / alunos
print (f'A média das idades é: {idaderesultado:.2f}')  