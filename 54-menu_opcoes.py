n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
resp = 0
while resp != 5:
    print('========Escolha uma das opções abaixo ========')
    print('''    [1] somar 
    [2] multiplicar 
    [3] maior 
    [4] novos números 
    [5] sair do programa''')
    resp = int(input('Digite o número desejado: '))
    if resp == 1:
        print ('A soma entre {} e {} é: {} '.format(n1, n2, n1+n2))
    elif resp == 2:
        print('A multiplicação entre {} e {} é: {} '.format(n1, n2, n1 * n2))
    elif resp == 3:
        print('O maior número entre {} e {} é: {} '.format(n1, n2, max(n1,n2)))
    elif resp == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif resp == 5:
        print('Saindo...')
    else:
        print('número inválido!')


