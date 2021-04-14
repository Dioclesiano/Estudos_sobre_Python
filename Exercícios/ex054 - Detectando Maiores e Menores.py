# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date
d = date.today().year

maior = 0
menor = 0
for c in range(1, 7):
    n = int(input('Digite o ano de seu nascimento » '))
    if d - n < 21:
        menor += 1
    else:
        maior += 1
print('Dentre as seis pessoas: {} são de maior(es) e {} não são de maior(es).'.format(maior, menor))
