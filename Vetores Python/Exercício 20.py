"""
20. Faça um programa que:
  - leia dois vetores (A e B) com cinco posições para números inteiros.
  - o programa deve, então, subtrair o primeiro elemento de A do último de B, armazenando o resultado num terceiro vetor, subtrair o segundo elemento de A do penúltimo de B, armazenando o resultado num terceiro vetor e assim por diante.
  - ao final, mostre o resultado do terceiro vetor
O índice de um dos vetores terá que ser decrementado (slide 2 de Vetor) , ou seja, você implementara ele manualmente.
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
a = []
b = []
c = []
for i in range (5):
  a.append(int(input(f'Digite o valor do vetor a[{i}]: ')))
  b.append(int(input(f'Digite o valor do vetor b[{i}]: ')))
p = len(b) -1
for i in range (len(a)):
  c.append(a[i] - b[p])
  p -= 1
print(a)
print(b)
print(c)