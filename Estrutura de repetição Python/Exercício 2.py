# 2. Faça um algoritmo que mostre o cumprimento ‘Olá ‘ para o nome de alguém (4 pessoas). Exemplo ‘Olá Mariana’. Pode implementar com o comando while ou for.

j = 0
nome = []
while j < 4:
 j = j + 1
 nome.append(input('Digite o nome: '))
print (f'\n\n')
i = 0 
while i < len(nome):
    print(f'- Olá {nome[i]}!')
    i = i + 1