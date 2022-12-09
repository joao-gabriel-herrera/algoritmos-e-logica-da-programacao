# 5. Faça um programa que leia números inteiros m e n e os elementos de uma matriz A de números inteiros de dimensão m x n e conte o número de elementos que são iguais a zero.

matriz = []
zeros = 0
linha = int(input('Insira quantas linhas você quer: '))
coluna = int(input('Insira quantas colunas você quer: '))
for l in range(linha):
    vet_linha = []
    for c in range(coluna):
        vet_linha.append(int(input(f'Digite o valor de [{l}][{c}]: ')))
        if vet_linha[c] == 0:
           zeros += 1
    matriz.append(vet_linha)
print(f'Na sua matriz exixtem {zeros} zero(s).')