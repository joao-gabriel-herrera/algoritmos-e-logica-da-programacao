# 18. Faça um programa que receba a medida do ângulo (em graus) formado por uma escada apoiada no chão e encostada na parede e a altura da parede onde está a ponta da escada. Calcule e mostre a medida dessa escada. Observação: as funções trigonométricas implementadas nas linguagens de programação trabalham com medidas de ângulos em radianos.

angulo = float(input('Insira o ângulo: '))
altura = float(input('Insira a altura: '))
import math
rad = (angulo * math.pi / 180)
escada = altura / math.sin(rad)
print (f'A medida da escada deve ser de: {escada:.2f}')