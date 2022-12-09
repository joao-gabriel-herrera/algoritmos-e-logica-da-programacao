"""
3. No estado de São Paulo, o IPVA (Imposto sobre a Propriedade de Veículos Automotores) possui valor da alíquota de imposto de 4%.
Dependendo do ano de fabricação, pode ocorrer isenção de IPVA, ou seja, não é pago nada, referente a este imposto.
O estado de São Paulo concede isenção a partir de 20 anos de fabricação.
Atendendo a 10 proprietários de automóveis, a partir dos anos de fabricação e dos valores dos carros, crie um programa utilizando a linguagem Python que, calcule e apresente:
  a) Quantidade de carros isentos.
  b) Valor do IPVA de cada carro.
  c) Média de valores dos carros.
  d) Total dos IPVAs pagos.
"""
carro_isento = 0
total_ipva = 0
valores_gerais = 0
for carro in range (10):
  valor_carro = float(input('Insira o valor do seu carro: R$ '))
  ano_fabricacao = int(input(f'Insira o ano de fabricação do seu carro: '))
  valores_gerais = valores_gerais + valor_carro
  print('\n')
  if ano_fabricacao <= 2002:
     print (f'Devido seu carro possuir mais de 20 anos o IPVA dele é Isento!\n\n')
     carro_isento = carro_isento + 1
  else:
    ipva = (valor_carro * (4/100))
    valor_com_imposto = valor_carro + ipva
    total_ipva = total_ipva + ipva
    print (f'Seu carro terá R$ {ipva:.2f} de IPVA para pagar neste ano corrente.\n\n')
valores_gerais = valores_gerais / 10
print(f'Quantidade de carros isentos: {carro_isento}')
print(f'Quantidade de alíquota recolhida: R$ {total_ipva:.2f}')
print(f'Média dos valores de carros: R$ {valores_gerais:.2f}')