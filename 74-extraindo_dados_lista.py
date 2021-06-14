'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []

while True:
    n = int(input('Digite um número: '))
    resp = input('Deseja continuar? [S/N]')
    lista.append(n)
    if resp in 'Nn':
        break
print('='*30)
print(f'Foram digitados {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Valores ordenados de forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')