'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
'''
from time import sleep #se der problema no sleep colocar no print 'flush=True'
def contador(i, f, p):
    if p < 0:
        p *= -1 #transforma p positivo
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ')
            c += p
            sleep(0.5)
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            c -= p
            sleep(0.5)
        print('FIM!')

    print('-='*20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inicio, fim, pas)
