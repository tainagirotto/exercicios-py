def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

frase = str(input('Digite uma frase: '))
escreva(frase)
