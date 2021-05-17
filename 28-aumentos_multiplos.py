# perguntar salário do funcionário e calcular o valor do seu aumento
# para salários superiores a 1.2500 -> aumento de 10%
# inferiores ou iguais -> aumento de 15%

sal = float(input('Digite seu salário atual: '))

if sal <= 1250:
    nsal = sal + (sal*15/100)
    print('Seu salário terá um aumento de 10% e passará a ser R$ {:.2f}' .format(nsal))
else:
    nsal = sal + (sal*10/100)
    print('Seu salário terá um aumento de 15% e passará a ser R$ {:.2f}' .format(nsal))