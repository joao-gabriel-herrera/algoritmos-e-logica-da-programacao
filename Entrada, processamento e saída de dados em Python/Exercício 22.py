# 22. Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.

vl_esp = float(input('Insira o valor do seu espetáculo: '))
vl_cvt = float(input('Insira o valor do convite: '))
qtd_cvt = round (vl_esp / vl_cvt)
print ('A quantidade de convites a ser vendida deve ser de: ',qtd_cvt,' convites.')