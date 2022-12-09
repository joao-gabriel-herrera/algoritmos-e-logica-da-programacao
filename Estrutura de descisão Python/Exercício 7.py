"""
7. Uma faculdade faz o pagamento de seus professores por hora/aula. Faça um algoritmo que receba o nível e a quantidade de hora/aula, calcule e exiba o salário de um professor e a frase a seguira tabela abaixo:
  - Professor Nível 1 - 11,00 reais por hora/aula, salário: ...
  - Professor Nível 2 - 15,00 reais por hora/aula, salário: ...
  - Professor Nível 3 - 19,00 reais por hora/aula, salário: ...
"""
nivel = int(input('Digite seu nível de professor: '))
aulas = float(input('Digite quantas horas/aulas você lecionou: '))
if nivel == 1 :
 salario = (11 * aulas)
 print(f'Seu salário será de R$ {salario:.2f}')
elif nivel == 2 :
 salario = (15 * aulas)
 print(f'Seu salário será de R$ {salario:.2f}')
elif nivel == 3 :
 salario = (19 * aulas)
 print(f'Seu salário será de R$ {salario:.2f}')
else:
  print('Você digitou um valor inválido!')