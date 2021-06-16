'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''
from time import sleep
alunos = []
temp = []
while True:
    nome = str(input('Nome: '))
    p1 = float(input('Nota 1: '))
    p2 = float(input('Nota 2: '))
    m = (p1 + p2)/2
    temp.append(nome)
    temp.append(p1)
    temp.append(p2)
    temp.append(m)
    alunos.append(temp[:])
    temp.clear()
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
print('-='* 30)
print(f'{"No.":<4}{"NOME":<10} {"MÉDIA":>8}')
print('-'*30)
for c, a in enumerate(alunos):
    print(f'{c:<4} {a[0]:<10} {a[3]:>8.1f}')
print('-'*30)
while True:
    id_nota = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    for c, a in enumerate(alunos):
        if id_nota == c:
            print(f'Notas de {a[0]}: {a[1]} e {a[2]}')
    if id_nota == 999:
        break
print('FINALIZANDO...')
sleep(1)
print('<< VOLTE SEMPRE >>')
