'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = {
        'Total': len(num),
        'Maior': max(num),
        'Menor': min(num),
        'Média': sum(num)/len(num),
    }
    if sit == True:
        if turma['Média'] >= 7:
            turma['Situação'] = 'Boa'
        elif turma['Média'] >= 5:
            turma['Situação'] = 'Razoável'
        else:
            turma['Situação'] = 'Ruim'
    return turma


resp = notas(5.5, 10.0, 8.0, sit=True)
print(resp)
help(notas)