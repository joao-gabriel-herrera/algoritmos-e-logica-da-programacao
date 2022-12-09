# 9. Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa de 1% para carros fabricados antes de 1990 e uma taxa de 1.5% para os fabricados de 1990 em diante, taxa esta incidindo sobre o valor de tabela do carro. Faça um algoritmo que leia o ano e o preço do carro, calcule e apresente o imposto a ser pago.

ano = int(input('Insira o ano de seu veículo (Todos digitos!: YYYY): '))
valor = float(input('Insira o valor de seu veículo: '))
if ano < 1990:
  imposto = valor * (1/100)
  print (f'O imposto a ser pago é de R$ {imposto:.2f}')
else:
  imposto = valor * (1.5/100)
  print (f'O imposto a ser pago é de R$ {imposto:.2f}')