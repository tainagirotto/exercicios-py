#Alistamento militar
# ler o ano de nascimento e informar:
# Se ele ainda vai se alistar ao serviço
# se é a hora de se alistar
# se já passou o tempo de alistamento.
# mostrar tbm o tempo que falta ou o tempo que passou do prazo.

from datetime import date

s = input('Você é do sexo feminino ou masculino? Responda [F/M]: ').upper()
if s == 'F':
    print('Você não precisa fazer o alistamento militar!')
elif s == 'M':
    print('Você deverá se alistar!')
    y = int(input('Informe seu ano de nascimento: '))
    age = date.today().year - y
    print('Você tem {} anos de idade' .format(age))
    if age == 18:
        print('\033[1;31m Faça seu alistamento militar!\033[m')
    elif age < 18:
        t = 18 - age
        print('Faltam \033[1;31m{} anos\033[m para seu alistamento militar!' .format(t))
    elif age > 18:
        t = age - 18
        print('Ainda não fez seu alistamento militar? Você está há \033[1;31m{} anos\033[m atrasado!' .format(t))

