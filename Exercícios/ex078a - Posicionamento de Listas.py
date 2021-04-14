'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
'''
# Solução 1

n = list()

for c in range(0,5):
    n.append(int(input(f'Digite o {c+1}º valor: ')))

for c, numero in enumerate(n):
    print('='*40)
    print(f'O número {numero} está na {c+1}ª posição')
print('='*40)
print()
print('~'*40)
print(f'O menor valor digitado foi »\033[31m {min(n)}\033[m «')
print(f'O maior valor digitado foi »\033[31m {max(n)}\033[m «')
print('~'*40)

# Solução 2

lista = []

menor = maior = 0
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}° número » '))
    lista.append(num)
    if c == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num

print(f'O menor número é {menor} e foi inserido na {lista.index(menor)+1}ª posição.')
print(f'O maior número é {maior} e foi inserido na {lista.index(maior)+1}ª posição.')
'''

# Solução 3

lista = []

menor = maior = 0
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}° número » '))
    lista.append(n)

    if c == 0:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print()
print(f'O menor valor é {menor} e aparece na(s) posição(ões) ', end='')
for k, v in enumerate(lista):
    if v == menor:
        print(f'{k+1}', end='  ')

print()

print(f'O maior valor é {maior} e aparece na(s) posição(ões) ', end='')
for k, v in enumerate(lista):
    if v == maior:
        print(f'{k+1}', end=' ')
