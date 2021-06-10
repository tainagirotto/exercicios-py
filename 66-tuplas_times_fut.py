times = ('Fortaleza', 'Atlético-PR', 'Atlético-GO', 'Bahia', 'Red Bull Bragantino', 'Fluminense',
         'Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians', 'Ceará', 'Santos', 'Cuiabá', 'Sport',
         'São Paulo', 'Juventude', 'Internacional', 'Grêmio', 'América-MG', 'Chapecoense')

print('='*30)
print(f'\033[32m Apenas os 5 primeiros colocados:\033[m {times[0:5]}')
print('='*30)
print(f'\033[32m Os últimos 4 colocados da tabela: \033[m{times[-4:]}')
print('='*30)
print(f'\033[32m Times em ordem alfabética:\033[m {sorted(times)}')
print('='*30)
print(f'\033[32m O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição')
## ou
for posicao, time in enumerate(times):
    if time == 'Chapecoense':
        print(f'\033[32m O time da {time} está na {posicao+1}ª posição \033[m')
