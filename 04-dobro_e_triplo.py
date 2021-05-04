# Mostrar o dobro, o triplo e raiz quadrada de um número.
number = int(input('Digite um número: '))
dobro = number * 2
triplo = number * 3
raiz_quadrada = number ** (1/2)
print('O dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(dobro, triplo, raiz_quadrada))

# o pow(number, (1/2)) também calcula a raiz quadrada