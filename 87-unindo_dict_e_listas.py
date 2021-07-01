'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoa = {}
dados = []
s = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if pessoa['sexo'] not in 'FfMm':
        print('Erro! Digite apenas F ou M')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    dados.append(pessoa.copy())
    resp = str(input('Deseja continuar? [S/N]'))
    if resp not in 'NnSs':
        print('Erro! Digite apenas S ou N.')
        resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
media = s/len(dados)
print('-='*10, 'ANÁLISE DOS DADOS', '-='*10)
print(f'    A) Ao todo temos {len(dados)} pessoas cadastradas')
print(f'    B) A média de idade é de {media:.2f} anos')
print(f'    C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
       print(f' {p["nome"]}', end=' ')
print()
print(f'    D)Uma lista de pessoas com idade acima da média: ', end='')
for p in dados:
    for k, v in p.items():
        if p['idade'] >= media:
            print(f'       {k} = {v}', end='')
    print()
print('         <<< ENCERRADO >>>')
