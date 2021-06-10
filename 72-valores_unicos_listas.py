valores = list()
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('valor adicionado')
    else:
        print('valor nao adicionado')
    resp = input('Deseja continuar? [S/N]').upper()
    if resp == 'N':
        break
valores.sort()
print(valores)
