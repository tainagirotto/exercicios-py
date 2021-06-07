#Escreva um programa que leia 2 numeros inteiros e compare-os
# mostrando: O primeiro valor é maior, o segundo valor é maior e não existe valor maior, os dois são iguais.

print('=*' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('=*' * 20)
if n1 < n2:

    print('\033[1;34m O SEGUNDO número é maior\033[m')
elif n2 < n1:

    print('\033[1;34m O PRIMEIRO número é maior\033[m')
else:
    print('Não existe maior número, \033[1;34m{} e {} são iguais!\033[m' .format(n1, n2))
