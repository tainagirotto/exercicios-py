print('='*20)
print('LOJA SUPER BARATÃO')
print('='*20)
s = maiorv = menorp = cont = 0
nome_menorp = ' '
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    s += preco
    if preco > 1000:
        maiorv += 1
    if cont == 1:
        menorp = preco
        nome_menorp = nome
    else:
        if preco < menorp:
            menorp = preco
            nome_menorp = nome
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja cadastrar mais produtos? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('---FIM DO PROGRAMA---')
print(f'O total da compra foi {s}')
print(f'Temos {maiorv} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_menorp}a que custou {menorp}')



