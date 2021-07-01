'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
gols = []
dados_jogador = {}
dados_jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
c = 1
while c <= partidas:
    gol = int(input(f'  Quantos gols na partida {c}? '))
    c +=1
    gols.append(gol)
dados_jogador['gols'] = gols
dados_jogador['total'] = sum(gols)
print('-='*30)
print(dados_jogador)
print('-='*30)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados_jogador["nome"]}, jogou {len(dados_jogador["gols"])} partidas')
for i, n in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {n} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')
