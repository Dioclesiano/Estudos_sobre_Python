'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.
'''

lista = []
pares = []
impares = []

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número » '))

    if n % 2 == 0:
        pares.append(n)

    else:
        impares.append(n)

print()

lista.append(sorted(pares))     # Organizando crescentemente os números
lista.append(sorted(impares))   # Organizando crescentemente os números
print(f'A lista completa com todos os números pares e ímpares são {lista}')

print()
print(f'Os números pares encontrados foram \033[31m{sorted(pares)}\033[m')
print(f'Os números impares encontrados foram \033[32m{sorted(impares)}\033[m')
