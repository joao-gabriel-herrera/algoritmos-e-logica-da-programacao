# 6. Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

nomes = []
print ('Utilize letras minúsculas e sem acentos\n')
for i in range (3):
  nomes.append(input(f'Insira o {i+1}º nome: '))
busca = input('\nInsira o nome que você busca: ')
if busca in (nomes):
   print(f'\nO nome {busca} está na lista de nomes, na {i+1}º posição.')
else:
    print(f'\nO nome {busca} não está na lista')
