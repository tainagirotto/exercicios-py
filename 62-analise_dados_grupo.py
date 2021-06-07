maior18 = tot_m = tot_f = 0

while True:
    print('-' * 5, 'CADASTRO DE PESSOAS', '-' * 5)
    id = int(input('Idade: '))
    if id >= 18:
        maior18 += 1
    s = ' '
    while s not in 'MF':
        s = input('Sexo: [M/F]: ').strip().upper()[0]
    if s == 'M':
        tot_m += 1
    if s == 'F' and id < 20:
        tot_f += 1
    print('-'* 15)
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
       break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {tot_m} homens cadastrados')
print(f'E temos {tot_f} mulher com menos de 20 anos')










