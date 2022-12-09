# 2. Faça um programa que carregue uma matriz 2 x 2, que representa o salário de 4 funcionários, calcule e mostre a soma total de todos os elementos que será o montante pago pela empresa a esses funcionários.

matriz = []
soma = 0
for l in range (2):
  vet_lin = []
  for c in range (2):
    vet_lin.append(float(input(f'Insira o salário do funcionário da posição {l,c}: ')))
    soma += vet_lin[c]
  matriz.append(vet_lin)
print(f'A soma dos salários registrados é de R$ {soma:.2f}')