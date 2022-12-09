# 3. Faça um programa que receba a altura de várias pessoas. Encontre e apresente a altura da pessoa mais alta e da mais baixa e seus respectivos nomes. Para encerrar a entrada de dados, zero na altura, mas esta não poderá ser considerada como resposta da altura da pessoa mais baixa.

altura = float(input('Informe a altura ou digite 0 para encerrar: '))
mais_alto = 0
mais_baixo = 3
while altura > 0 :
      nome = input(f'Informe o nome: ')
      if altura >= mais_alto:
          mais_alto = altura
          nome1 = nome
      elif altura <= mais_baixo:
          mais_baixo = altura
          nome2 = nome
      altura = float(input('Informe a altura ou digite 0 para encerrar: '))
print(f'{nome1} é o(a) mais alto(a) com {mais_alto:.2f} metros.')
print(f'{nome2} é o(a) mais baixo(a) com {mais_baixo:.2f} metros.')