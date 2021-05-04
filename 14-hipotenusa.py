# 017 -calcule o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e
# mostre o comprimento da hipotenusa
import math

cateto1 = float(input('Cateto 1:'))
cateto2 = float(input('Cateto 2:'))

print('O valor da hipotenusa é: {:.2f}' .format(math.hypot(cateto1, cateto2)))
