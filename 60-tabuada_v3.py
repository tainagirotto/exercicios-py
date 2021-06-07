while True:
    print('='*15, 'TABUADA', '='*15)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 39)
    if n < 0:
        break
    for c in range(1, 11):
       print(f' {n} x {c} = {n*c}')
print('PROGRAMA ENCERRADO!')





