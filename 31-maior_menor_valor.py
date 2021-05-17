# ler 3 numeros e mostrar qual é o maior e qual é o menor.
import math

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

lista = [n1, n2, n3]

print('O menor número é {}' .format(min(lista)))
print('O maior número é {}' .format(max(lista)))




