# 4. Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

media = []
acima_media = 0
abaixo_media = 0
soma_media = 0
for i in range (10):
  media.append(float(input(f'Insira a média do {i+1}º aluno: ')))
  soma_media += media[i]
media_sala = soma_media / len(media)
for i in range(len(media)):
 if media[i] >= media_sala:
   acima_media += 1
 else:
   abaixo_media += 1
print(f'A nota média da sala é de {media_sala:.1f} pontos.')
print(f'A quantia de alunos acima da média é de {acima_media}')
print(f'A quantia de alunos abaixo da média é de {abaixo_media}')