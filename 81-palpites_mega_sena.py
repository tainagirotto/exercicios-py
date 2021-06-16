'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import sample
from time import sleep
print('='*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('='*30)
qntde = int(input('Quantos jogos você quer que eu sorteie? '))
print('-'*5, f'SORTEANDO {qntde} JOGOS', '-'*5)
lista_numeros = []
c = 1
while c <= qntde:
    lista_numeros.append(sorted(sample(range(1, 60), 6)))
    c +=1
for i, v in enumerate(lista_numeros):
    sleep(1)
    print(f'Jogo {i+1}: {v}')



