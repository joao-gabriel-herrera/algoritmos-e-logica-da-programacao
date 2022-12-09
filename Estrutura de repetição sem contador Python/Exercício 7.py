"""
7. No final do ano muitas pessoas compram presentes. Faça um programa que registre alguns dados das pessoas, usando como critério de parada a letra ‘n’, para a pergunta “Deseja cadastrar outro (‘s’/’n’)?”, para identificar o perfil dos compradores numa loja de roupas e apresente como resultado a:
  a) Quantidade de mulheres e de homens;
  b) Quantidade de mulheres e de homens abaixo e acima de 18 anos.
"""
homens = 0
homensabaixo = 0
homensacima = 0
mulheres = 0
mulheresabaixo = 0
mulheresacima = 0
continuar = input('Deseja cadastrar um cliente? (S/N)? ')
while continuar == 'S' or continuar == 's' :
  input('Insira seu nome: ')
  sexo = input('Insira seu sexo (M ou F): ')
  if sexo == 'm' or sexo == 'M':
    homens = homens + 1
  elif sexo == 'f' or sexo == 'F':
    mulheres = mulheres + 1
  else:
    print('Sexo inválido, refaça o cadastro!')
    continue
  idade = int(input('Insira sua idade: '))
  print()
  if idade <= 18 and (sexo == 'm' or sexo == 'M'):
   homensabaixo = homensabaixo + 1
  if idade <= 18 and (sexo == 'f' or sexo == 'F'):
   mulheresabaixo = mulheresabaixo + 1
  if idade > 18 and (sexo == 'm' or sexo == 'M'):
   homensacima = homensacima + 1
  if idade > 18 and (sexo == 'f' or sexo == 'F'):
   mulheresacima = mulheresacima + 1
  continuar = input('Deseja cadastrar outro cliente (S/N)? ')
  print()

print(f'Quantidade Total de Mulheres: {mulheres}')
print(f'Quantidade Total de Homens: {homens}')
print(f'Quantidade de Mulheres até 18 anos: {mulheresabaixo}')
print(f'Quantidade de Mulheres acima de 18 anos: {mulheresacima}')
print(f'Quantidade de Homens até 18 anos: {homensabaixo}')
print(f'Quantidade de Homens acima de 18 anos: {homensacima}')