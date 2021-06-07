print('='*10, 'SEQUÊNCIA DE FIBONACCI', '='*10)
n = int(input('Quantos termos você quer mostrar? '))
'''
f1 = 1
f2 = 0
f3 = 0
for n in range(0, n):
    print(f3, end=' - ')
    f3 = f1 + f2
    f1 = f2
    f2 = f3
print('FIM!')
'''
# com WHILE
t1 = 0
t2 = 1
print('{} - {}' .format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM!')





