'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
gols = []
dados_jogador = {}
geral = []
while True:
    dados_jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    c = 1
    while c <= partidas:
        gol = int(input(f'  Quantos gols na partida {c}? '))
        c +=1
        gols.append(gol)
        dados_jogador['gols'] = gols[:]
        dados_jogador['total'] = sum(gols)
    geral.append(dados_jogador.copy())
    gols.clear()
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print(geral)
print('-='*30)
print(f'cod', end=' ')
for i in dados_jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for i, j in enumerate(geral):
    print(f'{i:>3}', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'* 50)
while True:
    n = int(input('Deseja mostrar os dados de qual jogador? [999 para parar] '))
    if n == 999:
        break
    if n >= len(geral):
        print(f'ERRO! Não existe jogador com o código {n}')
    else:
        print(f'-- LEVANTAMENTO DOS DADOS DO JOGADOR {geral[n]["nome"]}: ')
        for i, g in enumerate(geral[n]['gols']):
            print(f'No jogo {i+1}, fez {g} gols.')
    print('-'* 50)
print(' <<< VOLTE SEMPRE >>>')