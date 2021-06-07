print('='*10, '10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA', '='*10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10-1) * razao
print('==== COM FOR ====')
for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM!')
print('==== COM WHILE ====')
c = primeiro_termo
while c <= decimo:
    print(c, end=' -> ')
    c += razao
print('FIM!')
