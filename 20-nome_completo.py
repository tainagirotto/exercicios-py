#Ler o nome completo de uma pessoa e mostrar:

name = input('Nome completo: ').strip()
letras = name.split()
print('Analisando seu nome....')
print('O nome com todas as letras maiúsculas: {} ' .format(name.upper()))
print('O nome com todas as letras minúsculas: {} ' .format(name.lower()))
print('Quantas letras ao todo sem considerar os espaços: {}' .format(len(''.join(letras))))
print('Quantas letras tem o primeiro nome: {}'.format(len(letras[0])))