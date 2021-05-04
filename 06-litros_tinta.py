# Calcular a área da parede e mostrar a quantidade de tinta necessária.
# Usar como referência: 1L de tinta para cada 2m

b = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = b * h
litro_tinta = a / 2
print('A área da parede é {} m2 e a quantidade de tinta que irá precisar é {} Litros '.format(a, litro_tinta))