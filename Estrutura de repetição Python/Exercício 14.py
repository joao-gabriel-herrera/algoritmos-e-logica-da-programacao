# 14. Faça um programa que calcule e apresente as tabuadas do 3 ao 7. Este exercício utiliza DUAS estruturas de repetição.

j= 3
while j >= 3 and j <= 7: 
  i = 1
  num = j
  while i < 11:
    print (f'{num} x {i} = {num * i}')
    i = i + 1
  print ('\n')
  j = j + 1