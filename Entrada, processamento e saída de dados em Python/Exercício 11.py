"""
11. Faça um programa que receba um número, calcule e mostre:
  - O número digitado ao quadrado
  - O número digitado ao cubo
  - A raiz do número digitado
  - A raiz cúbica do número digitado
"""
numero = float(input('Insira o número: '))
quadrado = numero **2
cubico = numero **3
raiz2 = numero ** (1/2)
raiz3 = numero ** (1/3)
print (f'O quadrado do numero {numero} é {quadrado:.2f} ')
print (f'O cubo do numero {numero} é {cubico:.2f} ')
print (f'A raiz quadrada do numero {numero} é {raiz2:.2f} ')
print (f'A raiz cúbica do numero {numero} é {raiz3:.2f} ')