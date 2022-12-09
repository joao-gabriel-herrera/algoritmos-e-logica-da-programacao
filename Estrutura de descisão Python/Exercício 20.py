"""
20. Faça um programa que mostre a data e a hora do sistema nos seguintes formatos: dia/mês/ano – mês por extenso e hora:minuto.
  Observação: from carrega um módulo/biblioteca da linguagem Python e o import é usado para informar qual objeto desta biblioteca queremos importar/carregar no nosso programa
"""
from datetime import datetime
hoje = datetime.now()
if hoje.month == 1:
    print(hoje.day,'/01/',hoje.year,'mês de Janeiro', hoje.hour,':',hoje.minute)
if hoje.month == 2:
    print(hoje.day,'/02/',hoje.year,'mês de Fevereiro', hoje.hour,':',hoje.minute)
if hoje.month == 3:
    print(hoje.day,'/03/',hoje.year,'mês de Março', hoje.hour,':',hoje.minute)
if hoje.month == 4:
    print(hoje.day,'/04/',hoje.year,'mês de Abril', hoje.hour,':',hoje.minute)
if hoje.month == 5:
    print(hoje.day,'/05/',hoje.year,'mês de Maio', hoje.hour,':',hoje.minute)
if hoje.month == 6:
    print(hoje.day,'/06/',hoje.year,'mês de Junho', hoje.hour,':',hoje.minute)
if hoje.month == 7:
    print(hoje.day,'/07/',hoje.year,'mês de Julho', hoje.hour,':',hoje.minute)
if hoje.month == 8:
    print(hoje.day,'/08/',hoje.year,'mês de Agosto', hoje.hour,':',hoje.minute)
if hoje.month == 9:
    print(hoje.day,'/09/',hoje.year,'mês de Setembro', hoje.hour,':',hoje.minute)
if hoje.month == 10:
    print(hoje.day,'/10/',hoje.year,'mês de Outubro', hoje.hour,':',hoje.minute)
if hoje.month == 11:
    print(hoje.day,'/11/',hoje.year,'mês de Novembro', hoje.hour,':',hoje.minute)
if hoje.month == 12:
    print(hoje.day,'/12/',hoje.year,'mês de Dezembro', hoje.hour,':',hoje.minute)