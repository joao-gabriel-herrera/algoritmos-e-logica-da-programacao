"""
10. Elabore um algoritmo que informando a idade de um nadador o mesmo terá condições de classificar em uma das seguintes categorias:
  - infantil = 5 - 10 anos;
  - juvenil = 11-17 anos;
  - adulto = maiores de 18 anos.
"""
idade = int(input('Insira a idade: '))
if idade >= 5 and idade <=10 :
 print(f'Sua idade se encaixa na categoria Infantil!')
elif idade >= 11 and idade <=17 : 
 print(f'Sua idade se encaixa na categoria Juvenil!')
elif idade > 18:
 print(f'Sua idade se encaixa na categoria Adulto!')
else:
  print('Você digitou um valor inválido!')