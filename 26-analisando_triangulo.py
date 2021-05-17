# ler o comprimento de três retas e diga se elas podem ou não formar um triângulo
# r1 == r2 r2 == r1 r3 == r1
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')

if r1 == r2 and r1 == r3 and r3 == r2:
    print('Nesse caso, todos os lados são iguais então podemos formar um triângulo\033[1;32m Equilátero!\033[m')
elif r1 == r2 or r2 == r3 or r3 == r2:
    print('Nesse caso, podemos formar um triângulo \033[1;32m Isósceles \033[m')
elif r1 != r2 and r1 != r3 and r3 != r2:
    print('Nesse caso, todos os lados são diferentes então o triângulo é\033[1;32m Escaleno!\033[m')
