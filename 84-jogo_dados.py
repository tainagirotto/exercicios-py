'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número no dado.
'''
from random import randint
from operator import itemgetter
from time import sleep
numbers = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)
           }
ranking = list()
for k, v in numbers.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('===== RANKING DOS JOGADORES =====')
ranking = sorted(numbers.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)




