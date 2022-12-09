"""
16. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber, seguindo estas regras:
  - a hora trabalhada vale a metade do salário mínimo.
  - o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
  - o imposto equivale a 3% do salário bruto.
  - o salário a receber equivale ao salário bruto menos o imposto.
"""
horas = float(input('Insira a quantidade de horas trabalhadas: '))
salariomin = float(input('Insira o valor do salário mínimo: '))
valorhora = (salariomin / 2)
salariobr = (valorhora * horas)
imposto = (salariobr * (3/100))
salarioliq = (salariobr - imposto)
print ('O valor do salário Liquído é de: ', salarioliq)
