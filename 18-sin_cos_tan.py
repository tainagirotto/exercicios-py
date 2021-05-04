# 018- Ler um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
a = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('O valor do seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}' .format(seno, cosseno, tangente))