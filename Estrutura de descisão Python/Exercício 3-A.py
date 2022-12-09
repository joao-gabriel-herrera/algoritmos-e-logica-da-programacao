# 3.a) Faça um algoritmo que leia duas notas de um aluno, calcule a média e verifique, apresentando, se está aprovado ou reprovado.

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
if ((nota1 + nota2) / 2) >= 6:
  print ('Parabéns, você foi aprovado!')
else:
  print ('Sinto muito! você foi reprovado!')