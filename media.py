# Ler dois valores e mostrar a média

p1 = float(input('Nota 1: '))
p2 = float(input('Nota 2: '))
media = (p1 + p2) / 2
print('A média do aluno foi: {}' .format(media))

# ou com função:

def find_average(nums):
    if nums == [] or nums == 0:
       return 0
    else:
     average = sum(nums)/ len(nums)
     return average

print(find_average([1, 3, 5, 7]))