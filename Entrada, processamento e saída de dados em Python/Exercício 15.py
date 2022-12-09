"""
15. O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
  - o valor correspondente ao lucro do distribuidor;
  - o valor correspondente aos impostos;
  - o preço final do veículo.
"""
PF = float(input('Insira o preço de fábrica do veículo: '))
PLD = float(input('Insira o percentual do lucro do distribuidor sobre o veículo (Sem o símbolo!): '))
PI = float(input('Insira o percentual de imposto sobre o veículo (Sem o símbolo!): '))
LD = PF * (PLD/100)
VI = PF * (PI/100)
VF = PF + LD + VI
print (f'O Lucro do Distribuidor será de R${LD:.2f}')
print (f'O Valor do Imposto será de R${VI:.2f}')
print (f'O Preço Final deste veículo será de R${VF:.2f}')