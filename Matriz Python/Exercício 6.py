# 6. Faça um programa que carregue: *um vetor com oito posições com os nomes das lojas; * um outro vetor com quatro posições com os nomes dos produtos; * uma matriz (8 x 4) com os preços de todos os produtos em cada loja. O programa deve mostrar todas as relações (nome da loja - nome do produto e preço), nas quais o preço não ultrapasse R$ 120,00.

nl = []
np = []
preco = []
for x in range(8):
    nl.append(input(f'Insira o nome da {x+1}º loja: '))
for y in range(4):
    np.append(input(f'Insira o nome do {y+1}º produto: '))
for l in range(len(nl)):
 vet_lin = []
 for c in range(len(np)):
   vet_lin.append(float(input(f'Insira o valor do {c+1}º produto da {l+1}º loja: R$ ')))
 preco.append(vet_lin)
print('=-'*3)
for z1 in range(len(preco)):
  for z2 in range(len(preco[0])):
    if preco[z1][z2] <= 120:
      print(f'Na loja {nl[z1]} o produto {np[z2]} tem um valor de R$ {preco[z1][z2]:.2f}')