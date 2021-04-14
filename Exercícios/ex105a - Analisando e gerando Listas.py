'''
Faça um programa que tenha uma função NOTAS() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação(opcional)

Adicionar também as docstrings da Função.

def NOTAS(lista):

    menor = 0
    maior = 0
    for k, v in enumerate(lista):
        if k == 0:
            menor = v
        else:
            if v < menor:
                menor = v


    for k, v in enumerate(lista):
        if k == 0:
            maior = v
        else:
            if v > maior:
                maior = v

    print(f'A maior nota registrada foi {maior} enquanto que a menor nota foi {menor}')

# Programa Principal
lista = []

nome = str(input('Digite o seu nome » '))

somanota = 0
cont = 1
while True:
    notas = int(input(f'Digite a nota \033[31m{cont}\033[m do aluno {nome} » '))
    lista.append(notas)

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S[Sim] ou N[Não] ')

    if resp in 'N':
        break

    somanota += notas
    cont += 1

print()
print('*'*80)
print(f'Registramos {cont} notas e a média é de {somanota/cont}')
NOTAS(lista)
print('*'*80)

'''

from ex105 import notas
disciplinas = ['Português', 'Matemática', 'Ciências', 'Geografia']
aproveitamento = []
nota = []
aluno = []

stop = ' '
while stop not in 'S' and 'SAIR':
    aluno.append(str(input('Digite o nome do Aluno » ')))
    for c in range(0, len(disciplinas)):
        nota.append(float(input(f'Digite a nota de {disciplinas[c]} » ')))
    aproveitamento.append(nota[:])
    nota.clear()
    stop = str(input('Digite "S" ou "SAIR" » ')).upper()

exibir = ' '
while exibir not in 'SN':
    exibir = str(input('Digite [S] para exibir resultados ou [N] para não exibir » ')).upper()[0]
    if exibir in 'S':
        situacao = True
    elif exibir in 'N':
        situacao = False
    else:
        print('Entrada Inválida! Tente novamente')
notas(aluno, aproveitamento, situacao)
