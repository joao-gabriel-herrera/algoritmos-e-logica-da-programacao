# 9. Faça um algoritmo que conheça 4 preços de produtos, some-os e mostre o resultado. Pode implementar com o comando while ou for.

i = 0
precof = 0
while i < 4:
  preco = float(input('Insira o valor do produto: '))
  precof = precof + preco
  i = i + 1
print (f'A soma dos produtos inseridos é de R$ {precof:.2f}')