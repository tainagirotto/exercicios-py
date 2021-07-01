'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
'''
def voto(ano):
    from datetime import date
    print('-='* 15)
    id = date.today().year - ano
    if id < 16:
        return f'Com {id} anos: NÃO VOTA!'
    elif 16 <= id < 18 or id > 65:
        return f'Com {id} anos: VOTO OPCIONAL!'
    else:
        return f'Com {id} anos: VOTO OBRIGATÓRIO!'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))