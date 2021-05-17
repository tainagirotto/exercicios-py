# velocidade do carro
# mais de 80 km = multado
# 7 reais para cada km acima do limite

vel = float(input('Velocidade do carro em km: '))

if vel > 80:
    print('MULTADO!')
    valor_multa = (vel - 80) * 7
    print('O valor da multa é de R$ {:.2f} ' .format(valor_multa))
else:
    print('Parabéns, você está dentro do limite de velocidade')


