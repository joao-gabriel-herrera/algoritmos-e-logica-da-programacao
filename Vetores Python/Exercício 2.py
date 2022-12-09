# 2. Faça um programa que calcule e apresente a média de alturas de uma sala de 35 alunos. Informe também quantos alunos e quais (índice/posição) são os que possuem idade superior a 25 anos.​ Use dois vetores, um para altura e outro para idade. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

soma_altura = 0
altura = []
idade= []
qtd_alunos = 0
for i in range (5):
  altura.append(float(input('Insira sua altura: ')))
  idade.append(int(input('Insira sua idade: ')))
  soma_altura = soma_altura + altura[i]
media = soma_altura / len(altura)
print(f'A média das alturas é de {media:.2f} metros.')
for i in range(len(idade)): 
  if idade[i] > 25:
    print ('O aluno nº', i, 'possui', idade[i], 'anos.')
    qtd_alunos += 1
print('Foram encontrados', qtd_alunos, 'alunos maiores de 25 anos.')