import random
from time import sleep

print('=' *15, 'JOKENPO', '='*15)
opcoes = print('''
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')
jogador = int(input('Qual vai ser sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = random.randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if jogador == maquina:
    print('EMPATE!')
elif jogador == 0 and maquina == 1:
    print('A máquina GANHOU!')
elif jogador == 0 and maquina == 2:
    print('Você ganhou!! ')
elif jogador == 1 and maquina == 0:
    print('Você ganhou!!')
elif jogador == 1 and maquina == 2:
    print('A máquina ganhou!!')
elif jogador == 2 and maquina == 0:
    print('Você ganhou!!')
elif jogador == 2 and maquina == 1:
    print('Você ganhou!!')
else:
    print('Você digitou um número inválido')

print('A maquina escolheu a opção {}' .format(itens[maquina]))


