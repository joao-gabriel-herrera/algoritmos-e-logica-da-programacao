"""
19. Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:
  - o valor de cada quilowatt;
  - o valor a ser pago por essa residência;
  - o valor a ser pago com desconto de 15%.
"""
vl_sl = float(input('Insira seu salário: '))
qt_qw = float(input('insira a quantidade de quilowatts: '))
vl_qw = (vl_sl / 5)
vl_rs = (vl_qw * qt_qw)
vl_des = (vl_rs * (15 / 100))
vl_desct = (vl_rs - vl_des)
print (f'O valor de cada Quilowatt é de: R$ {vl_qw:.2f}')
print (f'O valor da conta é de: R$ {vl_rs:.2f}') 
print (f'O valor com desconto é de: R$ {vl_desct:.2f}') 