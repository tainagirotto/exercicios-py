# ler uma frase e dizer se ela é um palindromo (lendo de tras para frente é a mesma coisa) ps: desconsidere os espaços.
#ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.

frase = input('Escreva uma frase: ').strip().split()
junto = ''.join(frase)
print(junto)
inverso = junto[::-1]
print(inverso)
if junto == inverso:
    print('é um palíndromo!')
else:
    print('não é um palíndromo')

## ou
#  for letra in range(len(junto) -1, -1, -1):
# inverso += junto[letra]


