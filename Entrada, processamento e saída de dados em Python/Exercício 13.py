"""
13. Sabe-se que:
 * pé = 12 polegadas
 * 1 jarda = 3 pés
 * 1 milha = 1760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
  - Polegadas;
  - Jardas;
  - Milhas.
"""
pes = float(input('Insira o número em pés: '))
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760
print (f'O valor dos pés em polegadas é {polegadas:.2f} ')
print (f'O valor dos pés em jardas é {jardas:.2f} ')
print (f'O valor dos pés em milhas é ~{milhas:.2f} ')