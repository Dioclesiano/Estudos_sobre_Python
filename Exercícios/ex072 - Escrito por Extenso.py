'''
Crie um programa que tenha uma tupla
totalmente preenchida com uma contagem por
extenso, de Zero até vinte. Seu programa deverá
ler um número pelo teclado (entre 0 e 20) e
mostrá-lo por extenso.
'''

n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
     'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n1 = int(input('Digite um número de 0 a 20 » '))
    if 0 <= n1 <= 20:
        break

print(f'O número "{n1}" é escrito por extenso » {n[n1]} «')


valor = int(input('Digite um valor inteiro » '))

tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
     'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

# Usando FOR
for c in range(0, 20):
    if c == valor:
        print(f'O número {valor} escreve-se por extenso: {tupla[c]}')

# Usando WHILE
valido = False
while valido == False:
    extenso = int(input('Digite um número » '))

    if 0 <= extenso <= 20:
        print(f'O número digitado digitado é {extenso} => {tupla[extenso]}')
        valido = True
    else:
        print(f'O número {extenso} não está na lista, tente novamente.')
