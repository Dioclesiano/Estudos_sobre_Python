# Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO.
# Desconsiderando os espaços.
# Ex: Ovo, apos a sopa, a sacada da casa, a torre da derrota,
# o lobo ama o bolo, anotaram a data da maratona.

'''
from time import sleep

frase = str(input('Digite um PALÍNDROMO: ')).strip().upper()

lista = frase.split() # O comando SPLIT() cria uma lista para que possa fazer separações de palavras e letras
junta_palavra = ''.join(lista) # O comando JOIN() uni as palavras em lista criadas pelo comando SPLIT()
junta_letra = '-'.join(junta_palavra) # Este comando faz a separação das letras.

invertendo = '\033[31m'
for c in range(len(junta_letra)-1, -1, -1):
    invertendo += junta_letra[c]

if junta_letra == invertendo:
    print('A frase digitada "{}" é um PALÍNDROMO. Veja:'.format(frase))
else:
    print('A frase digitada "{}" não é um PALÍNDROMO. Veja:'.format(frase))

print('Invertendo a frase "{}"'.format(frase))
print('Invertendo ...')
sleep(5)
print('»» {} \033[m««'.format(invertendo))
'''

palavras = input('Digite Palavras » ').upper().strip().split()
juntarPalavras = ''.join(palavras)
juntarLetras = ' '.join(juntarPalavras)

print()
print(f'Invertendo o nome {juntarPalavras} fica ')
for c in range(len(juntarLetras)-1, -1, -1):
    print(f'{juntarLetras[c]}', end=' ')

print()
