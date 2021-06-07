# ler o ano de nascimento de 7 pessoas e mostrar quantas ainda não atingiram a maioridade e quantas já são maiores.
# considerar maioridade: 21 anos.
from datetime import date

hoje = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = hoje - nasc
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoa(s) já atingiram a maioridade. ' .format(maior))
print('{} pessoa(s) ainda não atingiram a maioridade. ' .format(menor))
