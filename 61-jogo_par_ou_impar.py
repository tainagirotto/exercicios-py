from random import randint
from time import sleep
print('='*10, 'JOGO DO PAR OU ÍMPAR', '='*10)
tot_vencedor = 0
while True:
    n_jogador = int(input('Digite um valor: '))
    valor_jogador = input('Par ou ímpar? [P/I] ').upper()
    print('*' * 15)
    n_pc = randint(0, 10)
    tot = n_pc + n_jogador
    par = tot % 2 == 0
    impar = tot % 2 != 0
    while valor_jogador not in 'PI':
        valor_jogador = input('Par ou ímpar? [P/I] ').upper()[0]
    if par and valor_jogador == 'I':
        sleep(1)
        print('VOCÊ PERDEU!')
        print(f'Você jogou {n_jogador} e o computador {n_pc}. O total de {tot} que é PAR')
        break
    if impar and valor_jogador == 'P':
        sleep(1)
        print('VOCÊ PERDEU!')
        print(f'Você jogou {n_jogador} e o computador {n_pc}. O total de {tot} que é ÍMPAR')
        break
    if par and valor_jogador == 'P':
        sleep(1)
        print('VOCÊ VENCEU!')
        print(f'Você jogou {n_jogador} e o computador {n_pc}. O total de {tot} que é PAR')
        tot_vencedor += 1
    if impar and valor_jogador == 'I':
        sleep(1)
        print('VOCÊ VENCEU!')
        print(f'Você jogou {n_jogador} e o computador {n_pc}. O total de {tot} que é ÍMPAR')
        tot_vencedor += 1
sleep(1)
print(f'GAME OVER! Você venceu {tot_vencedor} vezes')



