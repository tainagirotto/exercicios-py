n = int(input('Digite um número: '))
div = 0
for c in range(1, n+1):
    if n%c == 0:
        print('\033[34m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), '\033[m', end=' ')
print('\n O número {} é divisível por {} números' .format(n, div))
if div == 2:
    print('Por isso, ele é primo!')
else:
    print('Por isso, ele não é primo!')


