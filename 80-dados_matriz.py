'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
maior = somapar = terceira_coluna = 0

for l in range(0,3):
    for c in range(0,3):
           matriz[l][c] = int(input(f'Digite o número: [{l}, {c}]: '))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            terceira_coluna += matriz[l][2]
        if l == 1:
            maior = max(matriz[1])
    print()
print('-'*30)
print(f'a) A soma dos valores pares é {somapar}')
print(f'b) A soma dos valores da terceira coluna é: {terceira_coluna}')
print(f'c) Maior valor da segunda linha: {maior}')
