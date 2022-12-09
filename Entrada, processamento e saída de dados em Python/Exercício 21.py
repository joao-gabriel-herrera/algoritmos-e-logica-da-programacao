"""
21. Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. Lembre-se de que:
  - para quatro e meia, deve-se digitar 4.30;
  - os minutos vão de 0 a 59.
"""
hora = float(input('Insira a hora: '))
hora_int =(hora // 1)
minutos = (hora - hora_int)
minuto_novo = (minutos * 100)
print (f'A hora digitada tem: {minuto_novo:.0f} minutos')