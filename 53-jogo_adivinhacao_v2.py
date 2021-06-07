import random
from time import sleep

numero_pc = random.randint(0, 10)
numero_Jogador = 0
tentativas = 0
while numero_Jogador != numero_pc:
     numero_Jogador = int(input('Escolha um número de 1 a 10: '))
     tentativas += 1
     if numero_Jogador < numero_pc:
         print('Dica: O número é maior!')
     if numero_Jogador > numero_pc:
        print('Dica: O número é menor!')
if numero_Jogador == numero_pc:
    print('PROCESSANDO....')
    sleep(1)
    print('Parabéns, você ganhou!')

print('O número escolhido pelo PC foi {}' .format(numero_pc))
print('Foram necessários {} tentativas para vencer!' .format(tentativas))