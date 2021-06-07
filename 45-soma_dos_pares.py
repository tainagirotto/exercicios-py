# ler 6 numeros inteiros e mostrar a soma apenas do que forem par. Se for ímpar desconsiderar.
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('n{}: '.format(c)))
    if n%2 == 0:
        s += n
        cont += 1
print('Você informou {} número(s) pare(s) e a soma entre eles é {}' .format(cont,s))

