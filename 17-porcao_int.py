# 016- Ler um número real e mostrar na tela a porção inteira
from math import trunc
num = float(input('Digite um número real: '))
print('A porção inteira desse número é: {}' .format(trunc(num)))
