n = int(input('Digite o número que deseja saber o fatorial: '))
f = 1
c = n
while c > 1:
    f *= c
    c -= 1
print('Usando while: O fatorial de {}! é {} '.format(n,f))
## or

for c in range(c, 1, -1):
    f *=c
print('Usando for: O fatorial de {}! é {} ' .format(n,f))

## or
from math import factorial

f = factorial(n)
print('Usando math: O fatorial de {}! é {} ' .format(n,f))