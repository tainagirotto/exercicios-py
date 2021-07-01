'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
dados = {}

dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nasc # ou import datetime e coloca datetime.now().year
dados['ctps'] = int(input('Carteira de trabalho (digite 0 se não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    ano_aposentadoria = dados['contratação'] + 35
    dados['aposentadoria'] = ano_aposentadoria - ano_nasc
for k, v in dados.items():
    print(f'    - {k} tem o valor de {v}')