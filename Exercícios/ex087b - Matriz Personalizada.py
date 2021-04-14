'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somacoluna = 0
maior = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o número do quadrante [\033[31m{l+1}\033[m, \033[31m{c+1}\033[m] na matriz » '))
        soma += matriz[l][c]

print()
print('=-='*15)
print()

print('Valores distribuídos na Matriz')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[7;30m[{matriz[l][c]:^5}]\033[m', end='')
    print()

print()
print(f'A soma total dos valores inserido na Matriz é -> \033[31m{soma}\033[m <- ')

# Calculando a soma dos valores da terceira coluna
for l in range(0, 3):
    somacoluna += matriz[l][2]

print(f'A soma dos valores da teceira coluna -> \033[31m{somacoluna}\033[m <- ')

# Descobrindo o maior valor da segunda linha
for c in range(0, 3):
    if c == 0:
        matriz[1][c] = 0
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print(f'O maior número digitado na segunda linha -> \033[31m{maior}\033[m <- ')
