# Ler uma frase e mostrar na tela:

phrase = input('Digite uma frase: ').strip().lower()
print('Quantas vezes aparece a letra A: {}' .format(phrase.count('a')))
print('Em que posição ela aparece a primeira vez: {} '.format(phrase.find('a')))
print('Em que posição ela aparece a última vez: {} '.format(phrase.rfind('a')))
