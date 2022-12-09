# 13. Faça um algoritmo que leia o preço de 20 TV, determine e apresente a média dos preços que possuem valor maior que R$ 1000. Pode implementar com o comando while ou for.

tv = 0
valor_cont = 0
banco_valor = 0
while tv < 20:
  valor = float(input('Insira o valor da TV: '))
  if valor > 1000:
    banco_valor = banco_valor + valor
    valor_cont = valor_cont + 1
  tv = tv + 1
media = banco_valor / valor_cont
print(f'A média de valor das tv acima de R$ 1000,00 é de {media:.2f}')