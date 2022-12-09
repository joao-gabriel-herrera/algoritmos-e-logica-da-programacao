"""
2. Um professor de uma instituição de ensino, pediu ajuda para você organizar as notas dos alunos de três provas, que ocorreram ao longo do semestre. Ele informou que para o aluno ser aprovado é necessário ter a média das notas igual a 7.
O professor passou algumas diretrizes:
  a) media = 7
  b) numero_provas = 3
  c) O aluno é considerado reprovado de forma direta, se não realizar uma das provas.
Crie um programa utilizando a linguagem Python, para calcular e apresentar a média e avaliar a situação de aprovação ou não do aluno. Adote os nomes das variáveis apresentadas para o desenvolvimento e siga as diretrizes.
"""
p1 = float(input('Insira a nota da 1º prova (caso o aluno não tenha feito escreva 0): '))
p2 = float(input('Insira a nota da 2º prova (caso o aluno não tenha feito escreva 0): '))
p3 = float(input('Insira a nota da 3º prova (caso o aluno não tenha feito escreva 0): '))
if p1 == 0 or p2 == 0 or p3 == 0:
  print ('Infelizmente por não ter realizado uma das provas você foi Reprovado!')
else:
  media = (p1+p2+p3) / 3
  if media >= 7:
    print(f'O aluno foi Aprovado com uma média de {media:.2f} pontos!')
  else:
    print (f'O aluno foi Reprovado devido a média de {media:.2f} pontos!')