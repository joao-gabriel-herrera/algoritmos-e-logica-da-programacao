# 3. Faça um programa que carregue uma matriz 3 x 2, que representa preços de produtos, crie OUTRA matriz que armazene todos os preços com 7% de aumento.

matriz = []
matriz2 = []
for l in range (3):
  vet_lin = []
  for c in range (2):
    vet_lin.append(float(input(f'Insira o valor do produto {l,c} : R$ ')))
  matriz.append(vet_lin)
for l in range (len(matriz)):
  vet_lin = []
  for c in range (len(matriz[0])): 
    vet_lin.append(matriz[l][c]*7/100+matriz[l][c])
    print(vet_lin[c], end='\t')
  matriz2.append(vet_lin)
  print()