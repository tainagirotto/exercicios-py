# programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 0.15 por km rodado

km = float(input('Quantidade de km percorrido: '))
dias = int(input('Quantidade de dias do aluguel: '))

preco_a_pagar = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é: {:.2f} reais' .format(preco_a_pagar))