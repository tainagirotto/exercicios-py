# ler o nome, idade e sexo de 4 pessoas e mostre:
# a média de idade do grupo
# nome do homem mais velho
# quantas mulheres tem menos de 21 anos.
tot = 0
soma = 0
media = 0
totf = 0
maiorid = 0
nome_velho = str
for c in range(1, 5):
    print('------- {}ª PESSOA -------'.format(c))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Digite seu sexo [M/F]: ').lower()
    tot = tot + 1
    soma += idade
    media = soma/tot
    if sexo == 'f' and idade < 21:
        totf = totf + 1
    if sexo == 'm' and idade > maiorid:
        maiorid = idade
        nome_velho = nome

print('A média das idades é: {:.0f} anos' .format(media))
print('O homem mais velho tem {} anos e se chama: {}' .format(maiorid, nome_velho))
print('Total de mulheres com menos de 21 anos: {}' .format(totf))



