"""
19. Faça um programa que:
  - insira dez números inteiros em um vetor
  - crie um segundo vetor, substituindo os números multiplos de 3 por "999""
  - exiba os dois vetores
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
vetor01 = []
vetor02 = []
for i in range(10):
  vetor01.append(int(input('Insira um valor: ')))
  if vetor01[i] % 3 == 0:
    vetor02.append(999)
  else:
    vetor02.append(vetor01[i])
print('Vetor 1:\n', vetor01)
print('Vetor 2:\n', vetor02)