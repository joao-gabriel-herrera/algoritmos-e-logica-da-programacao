"""
11. Faça um programa que:
  - preencha um vetor com sete números inteiros
Calcule e mostre:
  - os números múltiplos de 2;
  - os números múltiplos de 3;
  - os números múltiplos de 2 e de 3.
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
m2 = []
m3 = []
m2_m3 = []
for i in range(7):
  valor= int(input('Insira um valor: '))
  if valor % 2 == 0 and valor % 3 == 0:
    m2_m3.append(valor)
  elif valor % 2 == 0:
    m2.append(valor)
  elif valor % 3 == 0:
    m3.append(valor)
print('Multíplos de 2:\n', m2)
print('Multíplos de 3:\n', m3)
print('Multíplos de 2 e de 3:\n', m2_m3)