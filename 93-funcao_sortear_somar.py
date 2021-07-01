'''
Ex. Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
'''
from random import randint

def sorteia(lista):
    c = 1
    while c <= 5:
        n =  randint(1, 10)
        lista.append(n)
        c += 1
    print(f'Sorteando 5 valores da lista:', end=' ')
    for v in lista:
        print(f'{v}', end= ' ')
    print('PRONTO!')



def somaPar(lista):
    print(f'Somando os valores pares de {lista}', end= ' ')
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'temos {s}')

numeros = []
sorteia(numeros)
somaPar(numeros)
