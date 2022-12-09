# 17. Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. O banco criou uma taxa para a operação bancária de retirada que tem que pagar um imposto de 0.38% e o saldo inicial da conta está zerado.

salario = float(input('Insira seu salário: '))
vl_ch1 = float(input('Insira o valor do 1º cheque: '))
vl_ch2 = float(input('Insira o valor do 2° cheque: '))
imp_ch1 = (vl_ch1 * (0.38/100))
sq1 = vl_ch1 + imp_ch1
imp_ch2 = (vl_ch2 * (0.38/100))
sq2 = vl_ch2 + imp_ch2
saldo = (salario - sq1 - sq2)
print ('O valor do seu saldo é de: ', saldo)