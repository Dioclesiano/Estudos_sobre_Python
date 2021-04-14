'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = []

matriz1 = []
matriz2 = []
matriz3 = []

for c in range(1, 4):
    n1 = int(input(f'Digite o {c}º número da 1ª linha da Matriz » '))
    matriz1.append(n1)

print()

for c in range(1, 4):
    n2 = int(input(f'Digite o {c}º número da 2ª linha da Matriz » '))
    matriz2.append(n2)

print()

for c in range(1, 4):
    n3 = int(input(f'Digite o {c}º número da 3ª linha da Matriz » '))
    matriz3.append(n3)

print()

matriz.append(matriz1)
matriz.append(matriz2)
matriz.append(matriz3)
print()
print(f'A lista digitada é \033[31m{matriz}\033[m')
print()
print(matriz1)
print(matriz2)
print(matriz3)
