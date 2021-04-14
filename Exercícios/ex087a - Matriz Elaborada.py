'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.


matriz = []

s = 0
maior = 0
for linha in range(1, 4):

    linhas = []

    for coluna in range(1, 4):
        n = int(input(f'Digite o número da \033[31m{linha}ª linha e {coluna}ª coluna\033[m >>> [{linha},{coluna}] » '))
        linhas.append(n)
        s += n      # Função de soma de todos os valores inseridos

    matriz.append(linhas)

print()
print('A matriz formada com os números digitados é: ')
print(f'\033[35m{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}\033[m')

print()
print(f'A soma de todos os valores digitados -> {s}')
print(f'A soma dos valores inseridos na teceira coluna -> {matriz[0][2] + matriz[1][2] + matriz[2][2]}')

maior = matriz[1][0]
if matriz[1][1] > maior:
    maior = matriz[1][1]
if matriz[1][2] > maior:
    maior = matriz[1][2]

print(f'O maior número da segunda coluna é -> {maior}')
'''
linhas = []
matriz = []
pares = []

somaColuna = somaPar = maior = cont = 0
while cont < 9:
    for c in range(1, 4):
        numero = int(input(f'Digite o {cont+1}° número da Matriz referente a {c}° coluna » '))

        if numero % 2 == 0:
            somaPar += numero
            pares.append(numero)

        matriz.append(numero)
        cont += 1
    linhas.append(matriz[:])
    matriz.clear()

print()
print('A Matriz criada')
for c in range(0, len(linhas)):
    print(f'{linhas[c]}')

print()
print(f'A soma dos elementos da coluna 3 são » ', end='')
for c in range(0, 3):
    print(f'{linhas[c][-1]}', end=' = ' if c > 1 else ' + ')
    somaColuna += linhas[c][-1]

print(f'{somaColuna}', end='\n')
print(f'O(s) número(s) par(es) detectado(s) {pares} e a soma corresponde a {somaPar}')

for c in range(0, 3):
    if c == 0:
        maior = linhas[1][c]
    else:
        if linhas[1][c] > maior:
            maior = linhas[1][c]

print(f'O maior valor da segunda linha é » {maior}')
