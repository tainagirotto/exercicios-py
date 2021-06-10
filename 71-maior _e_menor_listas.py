valores = list()

for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}º valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} na(s) posição(es) ', end ='')

for c, v in enumerate(valores):
   if v == max(valores):
       print(f'{c}...', end='')
print()

print(f'O menor valor digitado foi {min(valores)} nas posição(es) ', end='')

for c, v in enumerate(valores):
   if v == min(valores):
       print(f'{c}...', end='')
print()




