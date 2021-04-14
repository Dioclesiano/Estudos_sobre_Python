'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.
'''
# Este exercício não ficou exatamente como foi pedido, mas serve para avaliar

boletim = []
lista = []

quantidade = int(input('Quantos cadastros deseja criar » '))

somaPort = somaMat = cont = 0
while cont < quantidade:
    lista.append(str(input('Digite o nome do aluno » ')))
    lista.append(float(input('Digite a nota de Português » ')))
    lista.append(float(input('Digite a nota de Matemática » ')))

    boletim.append(lista[:])
    lista.clear()

    cont += 1

print()
print(f'Alunos {"":<5} Portugues{"":<10} Matemática{"":>10}')
for l in range(0, quantidade):
    for c in range(0, 3):
        print(f'{boletim[l][c]}', end=f'{"":<10}')
    print()

print()
for c in range(0, len(boletim)):
    somaPort += boletim[c][1]
    somaMat += boletim[c][2]

print(f'A média da(s) nota(s) de português é(são) » {somaPort/quantidade}')
print(f'A média da(s) nota(s) de matemática é(são) » {somaMat/quantidade}')
print(f'A média geral das notas de português e matemática são » {(somaPort + somaMat)/quantidade}')
