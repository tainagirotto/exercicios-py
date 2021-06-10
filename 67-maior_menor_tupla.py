from random import randint


numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(numeros)
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')