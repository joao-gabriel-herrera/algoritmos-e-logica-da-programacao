"""
15. Faça um programa que:
  - preencha um vetor com quinze números
Determine e mostre:
  - o maior número e a posição por ele ocupada no vetor
  - o menor número e a posição por ele ocupada no vetor
Não use nenhuma função pronta da linguagem Python, a não ser len() e append().
"""
valor = []
maior = 0
menor = 0
for i in range (15):
  valor.append(int(input('Insira um valor: ')))
  if len(valor) == 1:
    maior = valor[i]
    menor = valor[i]
  else:
      if valor[i] >= maior:
        maior = valor[i]
      elif valor[i] <= menor:
        menor = valor[i]
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')