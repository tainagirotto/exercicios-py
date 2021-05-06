# Digitar um nome e mostrar: Primeiro e ultimo nome.

name = input('Digite seu nome: ')
name = name.split()
print(name)

print('First name: {}' .format(name[0]))
print('Last name: {}' .format(name[-1]))
