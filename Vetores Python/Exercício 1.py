# 1. Faça um programa que calcule e apresente a média de idades de uma sala de 35 alunos.​​

idade = [] 
soma_idade = 0
for i in range(3):
    idade.append(int(input(f'Informe a {i + 1}ª idade: ')))
    soma_idade = soma_idade + idade[i]
    print(i)
media = soma_idade / len(idade)
print(f'A média é {media:.2f} anos.')