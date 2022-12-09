"""
1.Em Python, crie um programa que leia a quantidade de linhas e colunas de uma matriz.
Digite valores da matriz utilizando o tipo de dado int.
Faça a soma dos valores que estão na diagonal principal, estes estarão armazenados nas linhas que são iguais as colunas, tem exeplo no slide de matriz. Apresente o resultado da soma.
Mostre a matriz no formato de linha e colunas, conforme foi visto em aula.
"""
lin = int(input('Insira a quantidade de linhas: '))
col = int(input('Insira a quantidade de colunas: '))
matriz = []
soma = 0
for l in range (lin):
 vet_lin = []
 for c in range (col):
   vet_lin.append(int(input(f'Insira o valor da posição ({l} , {c}): ')))
   if l == c:
    soma += vet_lin[c]
 matriz.append(vet_lin)
print('')
print(f'A soma dos valores da diagonal principal é igual a {soma}. E a matriz ficou da seguinte forma: ')
print('')
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end='\t')
    print('')