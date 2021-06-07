print('='*10, '10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA', '='*10)
resp = 1
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
total = 0
mais = 10
c = 1
while mais != 0:
    total = total + mais
    while c <= total:
         print('{} -> '.format(termo), end='')
         termo += razao
         c +=1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')
print('Progressão finalizada com {} termos mostrados.' .format(total))
print('='*20)






