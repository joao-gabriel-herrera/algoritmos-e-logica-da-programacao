# 4. Faça um programa para armazenar em uma matriz 5x2 preços. Encontre e apresente os ÍNDICES dos valores menores que 23 reais.

ind = []
for l in range (5):
 vet_lin = []
 for c in range (2):
   vet_lin.append(float(input(f'Insira o valor do produto {l,c}: R$ ')))
 ind.append(vet_lin)
for y in range(len(ind)):
  for z in range(len(ind[0])):
     if ind[y][z] < 23:
          print(f'Os produtos abaixo de R$ 23,00 estão na seguinte posição: {y,z}')  