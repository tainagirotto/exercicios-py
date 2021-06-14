'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
 conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
 três listas geradas.
'''
valores = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = input('Deseja continuar? [S/N]')
    if resp in 'nN':
        break

print(f'Os valores digitados foram {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')