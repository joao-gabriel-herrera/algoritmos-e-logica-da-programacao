# 10. Faça um programa que calcule e mostre a área de um círculo. Sabe-se que:
"""
area = pi * raio² ou 
area = 3.1415 * raio²
"""
raio = float(input('Digite o raio do círculo: '))
pi = 3.1415
resultado = pi * (raio ** 2)
print (f'A área do círculo é:  {resultado:.2f} m²')