# ler o sexo de uma pessoa mas só aceitar M ou F.
# Caso esteje errado pedir digitação novamente até ter um valor correto.

s = input('Digite F para feminino e M para masculino: ').strip().upper()[0]
while s not in 'MmFf':
    s = input('Dados inválidos. Informe novamente seu sexo: ')
print('Sexo {} registrado com sucesso' .format(s))