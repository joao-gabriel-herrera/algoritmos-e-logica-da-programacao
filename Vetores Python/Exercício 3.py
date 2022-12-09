# 3. Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a pessoa mais gorda e mais magra e apresente o nome o peso das mesmas.​ Use dois vetores, um para peso e outro para nome. Não use nenhuma função pronta da linguagem Python, a não ser len() e append().

nome = []
peso = []
pessoas = 10
for i in range (pessoas):
  nome.append(input('Insira seu nome: '))
  peso.append(int(input('Insira seu peso: ')))
  if len(nome) == 1:
    peso_gordo = peso[i]
    nome_gordo = nome[i]
    peso_magro = peso[i]
    nome_magro = nome[i]
  else:
      if peso[i] >= peso_gordo:
        peso_gordo = peso[i]
        nome_gordo = nome[i]
      if peso[i] <= peso_magro:
        peso_magro = peso[i]
        nome_magro = nome[i]
print(f'A pessoa mais gorda se chama {nome_gordo} com {peso_gordo} Kg.')
print(f'A pessoa mais magra se chama {nome_magro} com {peso_magro} Kg.')
