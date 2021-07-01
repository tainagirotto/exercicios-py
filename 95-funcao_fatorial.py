'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
'''

def fatorial(n=1, show=False):
    """
    -> Calcular o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end=' ')
        f *= c
    return f

print(f'{fatorial(5, True)}')
#help(fatorial)