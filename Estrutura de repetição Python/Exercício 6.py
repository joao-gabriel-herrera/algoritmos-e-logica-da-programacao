# 6. Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, sendo que a maioridade é obtida após completar 18 anos. Pode implementar com o comando while ou for.

i = 0
maiores = 0
while i < 10:
  idades = int(input('Insira sua idade: '))
  i = i + 1
  if idades >= 18:
    maiores = maiores + 1
print(f'\n')
print(f'{maiores} pessoas da sua lista são maiores de idade.')