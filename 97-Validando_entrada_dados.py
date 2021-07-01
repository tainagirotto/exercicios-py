'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
'''

def leiaInt(msg):
    valor = 0
    n = str(input(msg))
    while n.isnumeric() == False:
        print('ERRO! Digite um valor válido!')
        n = str(input(msg))
    if n.isnumeric():
        valor = int(n)
    return valor


n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
