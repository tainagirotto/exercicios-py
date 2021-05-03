# Valor com desconto de 5%

price = float(input('Digite o preço do produto: R$ '))
valor_desconto = (5*price)/100
valor_total = price - valor_desconto
print('O valor com desconto de 5% é R$ {:.2f}'.format(valor_total))
a_vista = price - (price*10)/100

print('Se você pagar a vista o produto sai com 10% de desconto, perfazendo um total de R$ {:.2f}' .format(a_vista))