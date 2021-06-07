# a vista no dinheiro ou cheque 10% de desconto
# a vista no cartao 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou + no cartão 20% de juros

price = float(input('Digite o preço do produto: '))
formas = print(''' Formas de pagamento
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartao,
[ 3 ] 2x no cartão ou 
[ 4 ] 3x ou + no cartão''')
pgto = int(input('Digite a forma de pagamento: '))
if pgto == 1:
    valor_desc = price - (price * 10/100)
    print('O valor com o desconto de 10% ficará: R$ {:.2f}' .format(valor_desc))
elif pgto == 2:
    valor_desc_cartao = price - (price * 5/100)
    print('O valor com desconte de 5% ficará: R$ {:.2f}' .format(valor_desc_cartao))
elif pgto == 3:
    valor_parcela = price / 2
    print('Você não tem desconto. O valor de cada parcela fica: R$ {:.2f}' .format(valor_parcela))
elif pgto == 4:
    valor_com_juros = price + (price * 20/100)
    print('Você pagará 20% de juros se a parcela for de 3x ou mais no cartão. Perfazendo '
          'um valor de: R$ {:.2f}' .format(valor_com_juros))
else:
    print('Valor inválido')