"""
16. Faça um programa que:
  - preencha dois vetores com de dez numeros cada
  - preencha um terceiro vetor com os números dos dois vetores anteriores ordenados em ordem crescente
"""
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
  vetor1.append(int(input('Insira um valor para o vetor 1: ')))
  vetor2.append(int(input('Insira um valor para o vetor 2: ')))
vetor3 = vetor1 + vetor2
vetor3.sort()
print('Os valores em ordem crescente são: ',vetor3)
