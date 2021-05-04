# 019 - um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
import random

aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno sorteado foi: ', random.choice(lista))

