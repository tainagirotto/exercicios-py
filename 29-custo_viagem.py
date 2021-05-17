# perguntar a distancia em km
# calcular o preço da passagem cobrando 0,50 por km para viagens até 200km e 0.45 para viagens mais longas

distancia = float(input('Qual a distância percorrida em km? '))
if distancia <= 200:
    valor_p = distancia * 0.50
else:
    valor_p = distancia * 0.45

print('Você vai fazer uma viagem de {} km. O preço da sua passagem será de: R$ {:.2f}'.format(distancia, valor_p))