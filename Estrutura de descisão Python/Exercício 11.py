# 11. Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. Mostre uma mensagem informando o saldo médio e o valor do crédito.

saldo_medio = float(input('Insira a seu saldo médio: '))
if saldo_medio >= 0 and saldo_medio <=200 :
 print(f'Devido ao seu saldo médio baixo (R$ {saldo_medio:.2f}), não conseguimos aprovar o crédito especial!')
elif saldo_medio >= 201 and saldo_medio <=400 : 
 especial = saldo_medio * (20/100)
 print(f'Parábens! devido ao seu saldo médio (R$ {saldo_medio:.2f}) conseguimos aprovar R$ {especial:.2f} de Crédito Especial!')
elif saldo_medio >= 401 and saldo_medio <=600 : 
 especial = saldo_medio * (30/100)
 print(f'Parábens! devido ao seu saldo médio (R$ {saldo_medio:.2f}) conseguimos aprovar R$ {especial:.2f} de Crédito Especial!')
elif saldo_medio >= 601 : 
 especial = saldo_medio * (40/100)
 print(f'Parábens! devido ao seu saldo médio (R$ {saldo_medio:.2f}) conseguimos aprovar R$ {especial:.2f} de Crédito Especial!')
else:
  print('Você digitou um valor inválido!')