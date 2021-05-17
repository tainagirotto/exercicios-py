# ler um ano e mostrar qual o ano bissexto

from datetime import date

year= int(input('Digite qual ano deseja saber ou coloque 0 para analisar o ano atual:'))

if year == 0:
    year = date.today().year
if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
