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
def notas(n):
    """
    Passando uma lista como parâmetro contendo diversas notas do aluno
    :param n: Lista de notas
    :return: Total de Registros, menor nota, maior nota e média da turma
    """
    dicionario = {}

    dicionario['Total'] = len(n)
    dicionario['Menor'] = min(n)
    dicionario['Maior'] = max(n)
    dicionario['Média'] = sum(n)/len(n)
    print(dicionario)


# Programa Principal
dict = dict()
list = list()

cont = 1
while True:
    n = str(input(f'Digite seu {cont}° número correspondente a nota de 0 à 100 -> [S] para Sair » '))
    if n.isnumeric():
        n = int(n)

        if n >= 0 and n <= 100:
            dict[cont] = n  # Adicionando as notas em um dicionário na ordem em que foram digitadas.
            list.append(n) # Adicionando as notas em uma lista na ordem em que foram digitadas.
            # Neste exercício usarei a Lista no Programa principal e criarei um dicionário da DEF.
        else:
            print('\033[31mNota Inválida! Digite uma nota de 0 à 100\033[m')

    else:
        if n.upper() in 'S':
            break

    cont += 1

print()
notas(list)
help(notas)