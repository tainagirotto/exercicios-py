#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal
print('=' * 40)
num = int(input('\033[1;32m Digite o número que deseja converter\033[m: '))
base_conversao = print('''
\033[1;32m Digite:
 [ 1 ] para converter em Binário,
 [ 2 ] para octal e
 [ 3 ] para Hexadecimal\033[m: 
''')
opcao = int(input('Sua opção: '))

print('=' * 40)

if opcao == 1:
    num_binario = format(num, "b")
    print('O número em binário é: \033[1; m{}' .format(num_binario))
elif opcao== 2:
    num_octal = format(num, "o")
    print('O número em octal é: \033[1; m{}'.format(num_octal))
elif opcao == 3:
    num_hex = format(num, "x")
    print('O número em hexadecimal é: \033[1; m{}'.format(num_hex))
else:
    print('\033[1;31m Número incorreto, digite somente o número 1, 2 ou 3!\033[m')