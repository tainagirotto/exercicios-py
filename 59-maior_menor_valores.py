resp = 'S'
totn = s = m = maior = menor = 0

while resp == 'S':
    n = int(input('Digite um número: '))
    totn += 1
    s = s + n
    if totn == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Deseja continuar? [S/N] ').upper().strip()
m = s/totn
print('O total de números digitados foi {}' .format(totn))
print('A soma dos valores digitados foi {}' .format(s))
print('A média dos valores digitados foi {}'.format(m))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitados foi {}'.format(menor))
