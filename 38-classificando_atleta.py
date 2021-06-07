# leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
# Até 9 anos: mirim
# até 14 anos: infantil
# ate 19 anos: junior
# ate 20 anos: senior
# > 20: master
from datetime import date
print('=' *15, 'CLASSIFICAÇÃO DOS ATLETAS', '='*15)
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('=' *57)
if idade <= 9:
    print('O atleta tem {} anos e irá competir na categoria MIRIM.' .format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e irá competir na categoria INFANTIL.' .format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e irá competir na categoria JUNIOR.'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos e irá competir na categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e irá competir na categoria MASTER.'.format(idade))


