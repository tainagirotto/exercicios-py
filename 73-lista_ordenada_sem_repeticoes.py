# crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista já na posição correta sem usar o sort()
# No final, mostrar a lista ordenada na tela

valores = []

for v in range(0, 5):
    n = int(input('Digite um valor:'))
    if v == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {valores}')