'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(nome='', gols=''):
    if nome == "":
        nome = '<desconhecido>'
    if gols == "" or gols.isnumeric() == False:
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'


n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
print(ficha(n, g))

