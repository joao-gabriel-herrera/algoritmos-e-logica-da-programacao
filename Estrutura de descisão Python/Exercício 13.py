"""
13. A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:

NOTA	                   PESO
Trabalho de laboratório	   2
Avaliação semestral        3
Exame final	               5

Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela

MÉDIA PONDERADA	       CONCEITO
8,0 <= média <= 10	   A
7,0 <= média < 8,0	   B
6,0 <= média < 7,0	   C
5,0 <= média < 6,0	   D
0,0 <= média < 5,0	   E

media_ponderada = (nota_traballho * 2 + avaliacao_semestral * 3 + exame_final * 5) / 10
"""
trabalho = float(input('Insira a nota do Trabalho de Laborátorio: '))
semestral = float(input('Insira a nota da Avaliação Semestral: '))
exame = float(input('Insira a nota do Exame Final: '))
mediap = ((trabalho * 2) + (semestral * 3) + (exame * 5)) /10
if mediap >= 8 and mediap <= 10:
  print (f'A média ponderada das atividades foi de {mediap:.2f} pontos e o conceito deste aluno é A')
elif mediap >= 7 and mediap < 8:
  print (f'A média ponderada das atividades foi de {mediap:.2f} pontos e o conceito deste aluno é B')
elif mediap >= 6 and mediap < 7:
  print (f'A média ponderada das atividades foi de {mediap:.2f} pontos e o conceito deste aluno é C')
elif mediap >= 5 and mediap < 6:
  print (f'A média ponderada das atividades foi de {mediap:.2f} pontos e o conceito deste aluno é D')
elif mediap >= 0 and mediap < 5:
  print (f'A média ponderada das atividades foi de {mediap:.2f} pontos e o conceito deste aluno é E')
else:
  print ('Você inseriu algum valor errado!')