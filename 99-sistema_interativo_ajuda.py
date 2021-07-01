'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

from time import sleep

cor = ('\033[m',       # 0- sem cor
       '\033[97;41m',  # 1- vermelho
       '\033[97;42m',  # 2- verde
       '\033[30;107m', # 3- branco
       '\033[97;44m',  # 4- azul
       )

def linha(msg, cores=0):
    tam = len(msg) + 4
    print(cor[cores], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cor[0], end='')
    sleep(1)

def manual(comando):
    linha(f' Acessando o manual do comando \'{c}\'', 4)
    print(cor[3], end='')
    help(comando)
    print(cor[0], end='')
    sleep(1)

while True:
    linha('SISTEMA DE AJUDA PyHELP', 2)
    c = str(input('Função ou biblioteca >'))
    if c.upper() == 'FIM':
        break
    else:
        manual(c)
linha('ATÉ LOGO', 1)

