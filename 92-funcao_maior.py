'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep

def maior(* num):
    c = maior = 0
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ')
        sleep(0.3)
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        c +=1
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-='*30)


maior(4,5,50,7,8,9)
maior(2,6,4,1)
maior(4, 9, 60, 20, 30, 10)
maior()
maior(5)