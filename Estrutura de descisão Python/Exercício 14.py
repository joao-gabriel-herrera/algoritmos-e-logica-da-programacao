"""
14. Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exigida é 6,0.

MÉDIA ARITMÉTICA	MENSAGEM
0 <= média < 3	    Reprovado
3 <= média < 6	    Exame
6 <= média <= 10	Aprovado
"""
nota1 = float(input('Insira a primeira nota : '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 6 and media <= 10:
  print (f'Devido a media {media:.2f} do aluno ele foi Aprovado!')
elif media >= 3 and media < 6:
  media2 = media
  pontos = 0
  while media2 < 6:
   pontos = pontos + 1
   media2 = media2 + 1  
  print (f'Devido a media de {media:.2f} ponto(s) do aluno ele ficou de exame, para que ele consiga ser aprovado ele precisa de mais {pontos:.0f} ponto(s)!')
elif media >= 0 and media < 3:
  print (f'Devido a media {media:.2f} do aluno ele foi Reprovado!')
else:
  print ('Você inseriu algum valor errado!')