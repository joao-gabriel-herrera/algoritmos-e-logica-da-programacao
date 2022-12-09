"""
15. Faça um programa para o curso de ADS (6 módulos), cada sala tem 30 alunos, calcule e apresente os seguintes itens:
  - Quantidade de homens e mulheres de cada módulo;
  - Média de idades de cada módulo;
  - Quantidade de homens e mulheres do curso todo;
  - Média de idades do curso todo.
Observação: este exercício utiliza DUAS estruturas de repetição.
"""
total_homens = 0
total_mulheres = 0
media_total = 0

for modulo in range(1,7):
  print(modulo,'º módulo:\n')  
  media_modulo = 0
  homem_modulo = 0
  mulher_modulo = 0
  
  for cont in range (30):
      sexo = input('Insira seu gênero (M ou F): ')
      if sexo == 'M' or sexo == 'm':
        total_homens = total_homens + 1
        homem_modulo = homem_modulo + 1
      elif sexo == 'F' or sexo == 'f':
        total_mulheres = total_mulheres + 1
        mulher_modulo = mulher_modulo + 1
      

  for idade in range (30):
      idade = int(input('Insira sua idade: '))
      media_modulo = media_modulo + idade
      print(media_modulo, media_total)

  media_total = media_total + media_modulo
       
  print('\n')
  print(modulo,'º módulo','.'*50)
  print()
  print(f'Quantidade de Homens: {homem_modulo}')
  print(f'Quantidade de Mulheres: {mulher_modulo} ')
  print(f'Média de idades: {media_modulo/6:.2f}')
  print()
print()
print(f'Quantidade de total de Homens no curso: {total_homens}')
print(f'Quantidade de total de Mulheres no curso: {total_mulheres}')
print(f'Média de idades: {media_total / (total_homens + total_mulheres) :.2f}')