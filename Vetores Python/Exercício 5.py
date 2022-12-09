# 5. Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

numeros =[]
for i in range (8):
  numeros.append(int(input('Insira um valor: ')))
for i in range(len(numeros)):
  if numeros[i] % 2 == 0:
    print(f'O numero que está na {i+1}ª posição ({numeros[i]}) é par')