# 4. Faça um algoritmo que leia o gênero de uma pessoa. Se for digitado M ou F, apresentar 'Gênero válido!'. Caso contrário, 'Gênero inválido!'.

genero = input('Qual seu gênero (M ou F)?: ')
if (genero == 'M' or genero == 'm') or (genero == 'F' or genero == 'f'):
  print ('Gênero Válido!')
else:
  print ('Gênero Inválido!')
