# fazer o pc escolher um numero aleatório entre 0 e 5 e pedir para o usuario tentar adivinhar qual foi
# escrever na tela se o usuario venceu ou perdeu

import random
from time import sleep

numero_pc = random.randint(0, 5)
numero_Jogador = int(input('Escolha um número de 1 a 5: '))
print('PROCESSANDO....')
sleep(3)
if numero_Jogador == numero_pc:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu, tente novamente')

print('O número escolhido pelo PC foi {}' .format(numero_pc))
