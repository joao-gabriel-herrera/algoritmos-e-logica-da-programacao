"""
18. Faça um programa que receba quatro valores: I, A, B e C. Desses valores, I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C obedecendo à tabela a seguir.

Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os números digitados sejam diferentes um do outro.

VALOR DE I	   FORMA A ESCREVER
1	           A, B e C em ordem crescente.
2	           A, B e C em ordem decrescente
3	           O maior fica entre os outros dois números.
"""
print(f'Menu de operações:\n')
print('1 - Ordem crescente')
print('2 - Ordem decrescente')
print(f'3 - O maior entre os outros 2\n')
I = int(input('Escolha a opção desejada: '))
a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))
if I == 1:
  if a < b and a < c:
    if b < c:
      print (f'A ordem crescente desses valores é: {a:.2f}, {b:.2f}, {c:.2f}')
    else:
      print (f'A ordem crescente desses valores é: {a:.2f}, {c:.2f}, {b:.2f}')
  if b < a and b < c:
    if a < c:
      print (f'A ordem crescente desses valores é: {b:.2f}, {a:.2f}, {c:.2f}')
    else:
      print (f'A ordem crescente desses valores é: {b:.2f}, {c:.2f}, {a:.2f}')
  if c < b and c < a:
    if a < b:
      print (f'A ordem crescente desses valores é: {c:.2f}, {a:.2f}, {b:.2f}')
    else:
      print (f'A ordem crescente desses valores é: {c:.2f}, {b:.2f}, {a:.2f}')
if I == 2:
  if a > b and a > c:
    if b > c:
      print (f'A ordem decrescente desses valores é: {a:.2f}, {b:.2f}, {c:.2f}')
    else:
      print (f'A ordem decrescente desses valores é: {a:.2f}, {c:.2f}, {b:.2f}')
  if b > a and b > c:
    if a > c:
      print (f'A ordem decrescente desses valores é: {b:.2f}, {a:.2f}, {c:.2f}')
    else:
      print (f'A ordem decrescente desses valores é: {b:.2f}, {c:.2f}, {a:.2f}')
  if c > b and c > a:
    if a > b:
      print (f'A ordem decrescente desses valores é: {c:.2f}, {a:.2f}, {b:.2f}')
    else:
      print (f'A ordem decrescente desses valores é: {c:.2f}, {b:.2f}, {a:.2f}')
if I == 3:
  if a > b and a > c:
    print (f'A ordem com o maior no meio fica desta forma: {b:.2f}, {a:.2f}, {c:.2f}')
  if b > a and b > c:
    print (f'A ordem com o maior no meio fica desta forma: {a:.2f}, {b:.2f}, {c:.2f}')
  if c > b and c > a:
    print (f'A ordem com o maior no meio fica desta forma: {a:.2f}, {c:.2f}, {b:.2f}')
else:
  print ('Opção Inválida!')
