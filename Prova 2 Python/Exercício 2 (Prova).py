"""
2. [5,50 pontos] Foi realizada uma pesquisa sobre algumas características físicas de ALGUNS habitantes de uma região, NÃO FOI INFORMADA A QUANTIDADE TOTAL, então use como critério de parada, idade igual a zero para encerrar a repetição. Preste atenção nesse detalhe, pois somente poderá usar a função append, quando for digitado uma idade válida.
Foram coletados os seguintes dados de cada habitante: idade, gênero (M/F), cor dos olhos (A - azuis ou V - verdes). Escolha se quer armazenar uma letra ou a palavra, para cor dos olhos.
Em Python crie um programa que leia esses dados, armazenando-os em vetores, uma para idade, outro para gênero (apenas uma letra) e outro para cor dos olhos.
Calcule e apresente:
  - Média de idades das pessoas com olhos verdes;
  - Quantidade de pessoas que foram entrevistadas com olhos verdes e quantidade com olhos azuis
  - Quantidade de pessoas do gênero masculino com idade entre 29 e 40 anos e que tenham olhos azuis.

Observação: pode usar o operador in e a função len()e a append() apenas. Outras funções prontas da linguagem Python, não serão aceitas.
Observação 2: Neste exercício apenas armazene os dados nos vetores, não é necessário manipular os dados nos vetores, use variáveis externas.
"""
qtd = int(input('Insira a quantidade de habitantes da região: '))
idades = []
generos = []
olhos = []
cont = 0
soma_olhos_verdes = 0
ovv =[]
ov = 0
oa = 0
pessoa_especial = 0
print('-'*30)
print(f'Para encerrar o programa digite uma idade menor ou igual a 0. \n')
while cont < qtd:
  idade = int(input('Insira sua idade: '))
  if idade != 0:
     idades.append(idade) 
     genero = input('Insira seu genêro (M ou F): ')
     if genero == 'm' or genero =='M' or genero == 'f' or genero =='F':
       generos.append(genero)
     else:
       print('Você digitou um genêro inválido! a coleta de dados será reiniciada!')
       idades.remove(idade)
       continue
     olho = input('Insira a cor de seus olhos ("A" para azul e "V" para verde): ')
     if olho == 'a' or olho =='A' or olho == 'v' or olho =='V':
       olhos.append(olho)
     else:
       print('Você digitou uma cor inválida! a coleta de dados será reiniciada!')
       idades.remove(idade)
       generos.remove(genero)
       continue
     if olho == 'v' or olho == 'V':
       ov += 1
       soma_olhos_verdes += idade
       ovv.append(idade)
     if olho == 'a' or olho == 'A':
       oa += 1
     if idade >= 29 and idade <= 40 and genero == 'm' or genero == 'M' and  olho == 'a' or olho == 'A':
       pessoa_especial += 1
     cont += 1
  else:
    break
if len(ovv) > 0:
 media_ov = soma_olhos_verdes / len(ovv)
else:
  media_ov = 0
print(f'\n\nMédia de idades das pessoas com olhos verdes: {media_ov:.2f}')
print(f'Quantidade de pessoas que foram entrevistadas com olhos verdes: {ov}')
print(f'Quantidade de pessoas que foram entrevistadas com olhos azuis: {oa}')
print(f'Quantidade de pessoas do gênero masculino com idade entre 29 e 40 anos e que tenham olhos azuis: {pessoa_especial}')
