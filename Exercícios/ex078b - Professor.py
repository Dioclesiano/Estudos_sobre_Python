'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

n = []

maior = 0
menor = 0
for c in range(0, 5):
    n.append(int(input('Digite um número » ')))

    if c == 0:
        menor = n[c]
        maior = n[c]
    else:
        if n[c] < menor:
            menor = n[c]
        elif n[c] > maior:
            maior = n[c]
print()
print(f'O menor número digitado foi » {menor} « na(s) posição(ões) ', end='')

for i,v in enumerate(n):
    if v == menor:
        print(f'{i+1},', end='')

print(f'\nO maior número digitado foi » {maior} « na(s) posição(ões) ', end='')

for i, v in enumerate(n):  # Nesse caso o 'i' é de índice e o 'v' é de valor, mas podem ser outros nomes
    if v == maior:
        print(f'{i+1},', end='')
