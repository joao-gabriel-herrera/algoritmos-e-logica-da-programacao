"""
17. Faça um programa que:
  - carregue dois vetores com 10 números cada
  - faça a multiplicação dos números na mesma posição
  - o resultado deverá ser adicionada em um terceiro vetor
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
a = []
b = []
c = []
for i in range (10):
  a.append(int(input(f'Digite o valor do vetor a[{i}]: ')))
  b.append(int(input(f'Digite o valor do vetor b[{i}]: ')))
for i in range (len(a)):
  c.append(a[i] * b[i])
print(a)
print(b)
print(c)