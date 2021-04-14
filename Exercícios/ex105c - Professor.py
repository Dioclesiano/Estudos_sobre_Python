'''
Faça um programa que tenha uma função NOTAS() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação(opcional)

Adicionar também as docstrings da Função.
'''
def notas(*n, sit=False):
    """
    -> Função para analisar notas e sutuações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)

    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)