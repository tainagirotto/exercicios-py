# Escreva um programa para aprovar o emprestimo de uma casa.
# O programa vai perguntar: O valor da casa, valor do salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

print('\033[1;36m=='* 5, 'VERIFIQUE SE SEU EMPRESTIMO SERÁ APROVADO', '=='* 5, '\033[m')

valor_casa = float(input('Digite o valor do imóvel: R$ '))
valor_sal = float(input('Agora digite o valor do salário do comprador: R$ '))
anos = int(input('Em quantos anos deseja pagar? '))

prest_mensal = valor_casa / (anos*12)
print('O valor da prestação mensal é {:.2f}' .format(prest_mensal))
porcentagem = prest_mensal*100 // valor_sal
print(porcentagem)
if porcentagem > 30:
    print('\033[1;31m Seu empréstimo foi NEGADO! A prestação mensal excedeu 30% do salário do comprador.\033[m')
else:
    print('\033[1;34m Seu empréstimo foi APROVADO!')




