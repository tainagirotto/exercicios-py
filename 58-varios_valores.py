totn = s = 0
'''
while n < 999:
    n = int(input('Digite um número inteiro e 999 para parar: '))
    if n != 999:
        totn += 1
        s += n
print('O total de números digitados foi: {} '.format(totn))
print('E a soma entre eles é: {} '.format(s))
'''

## ou com break

while True:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n == 999:
        break
    s +=n
    totn += 1
print(f'O total de números digitados foi: {totn}')
print(f'E a soma entre eles é: {s} ')