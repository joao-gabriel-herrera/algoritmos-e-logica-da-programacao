# 11. Faça um algoritmo que conheça 4 preços de produtos, calcule e mostre a média aritmética dos preços. Pode implementar com o comando while ou for.

i = 0
precof = 0
while i < 4:
  preco = float(input('Insira o valor do produto: '))
  precof = precof + preco
  i = i + 1
precoma = precof / i
print (f'A media de preço dos produtos inseridos é de R$ {precoma:.2f}')
