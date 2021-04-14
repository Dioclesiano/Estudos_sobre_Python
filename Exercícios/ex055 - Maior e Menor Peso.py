# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
# o menor peso lidos.

maior = 0
menor = 0
for c in range(1,6):
    p = int(input('Digite seu peso » '))

    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
        else:
            pass

print('O maior peso digitado foi » {} kg'.format(maior))
print('O menor peso digitado foi » {} kg'.format(menor))
