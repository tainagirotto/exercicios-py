# Ler dois valores e mostrar a média

p1 = float(input('Nota 1: '))
p2 = float(input('Nota 2: '))
media = (p1 + p2) / 2
print('A média do aluno foi: {:.1f}' .format(media))

if media >= 7:
    print('\033[1;32m APROVADO\033[m')
elif media >= 5 and media < 7:
    print('\033[1;33m RECUPERAÇÃO\033[m')
else:
    print('\033[1;31m REPROVADO!\033[m')

# ou com função:
'''
def find_average(nums):
    if nums == [] or nums == 0:
       return 0
    else:
     average = sum(nums)/ len(nums)
     return average

print(find_average([1, 3, 5, 7]))
'''