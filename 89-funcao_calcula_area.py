print('Controle de Terrenos ')
print('-'* 10)

def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} é de {a}m')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
