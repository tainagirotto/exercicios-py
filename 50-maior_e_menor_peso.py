# ler peso de 5 pessoas e mostrar o maior e o menor peso lido.
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso {}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi: {} '.format(maior))
print('O menor peso lido foi: {} '.format(menor))

