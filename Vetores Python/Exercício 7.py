# 7. Faça um algoritmo que calcule e apresente a média de alturas superior a 1,80 de 10 alunos. Informe também quantos e quais (índice/posição) são os alunos. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

altura = []
soma_altura = 0
alunos_grandes = 0
for i in range (10):
  altura.append(float(input(f'Insira sua altura: ')))
  if altura[i] > 1.8:
    soma_altura += altura[i]
    alunos_grandes += 1
media = soma_altura / alunos_grandes
print(f'\nExistem {alunos_grandes} alunos com altura maior que 1.80, a média das idades deles é de {media:.2f} e suas respectivas posições são:')
for i in range (len(altura)):
 if altura[i] > 1.8:
  print(f'{i+1}º Aluno')