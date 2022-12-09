# 3.b) Faça um algoritmo que calcule e apresente o que foi requerido no exercício 3.a) e também avalie a condição de aprovar/reprovar, apenas quando o aluno tem frequencia acima de 75%, este valor deve ser lido.

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
frequencia = float(input('Digite a frequência do aluno: '))
if (((nota1 + nota2) / 2) >= 6 ) and (frequencia >= 75):
  print ('Parabéns, você foi aprovado!')
else:
  print ('Sinto muito! você foi reprovado!')