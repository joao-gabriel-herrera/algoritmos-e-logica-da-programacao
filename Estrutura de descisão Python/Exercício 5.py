"""
5. Tendo como dados de entrada a altura e o gênero (M/F) de uma pessoa (M-masculino ou F-feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
 * masculino: (72.7 * altura) - 58;
 * feminino: (62.1 * altura) - 44.7
"""
genero = input('Digite seu gênero (M ou F): ')
altura = float(input('Digite a sua altura: '))
if (genero == 'M' or genero == 'm'):
   peso_ideal = (72.7 * altura)
   print(f'Seu peso ideal é de: {peso_ideal:.2f} kg') 
elif  (genero == 'F' or genero == 'f'):
   peso_ideal = (62.1 * altura)
   print(f'Seu peso ideal é {peso_ideal:.2f} kg')
else:
   print ('Você digitou um gênero inválido!')
