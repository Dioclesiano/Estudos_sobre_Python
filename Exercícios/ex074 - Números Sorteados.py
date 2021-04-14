'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''
from random import randint
# Criei uma variável COMPUTADOR que irá recever a tupla e seus valores

computador = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

maior = 0
menor = 0
for k, v in enumerate(computador):
    print(f'O {k+1}° número gerado foi {v}')
    if k == 0:
        menor = computador[0]
        maior = computador[0]
    else:
        if computador[k] < menor:
            menor = computador[k]
        elif computador[k] > maior:
            maior = computador[k]

print(f'O menor número sorteado foi {menor} e o maior foi {maior}.\n')

print('=!'*100)

# Outra maneira simplificada para exibir os menores e maiores valores de uma tupla
print()
print(f'Os 10 números sorteados foram » {computador} «')

print()
print(f'O menor número sorteado é » {min(computador)} «')
print(f'O maior número sorteado é » {max(computador)} «')
