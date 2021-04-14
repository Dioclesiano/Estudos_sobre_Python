# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem.
# Sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint

dado = {}
maior = 0

for c in range(0, 4):
    dado[f'jogador'] = randint(1, 6)

    if c == 1:
        dado['jogador'] = 1

    else:
        if dado['jogador'] > maior:
            maior = dado['jogador']

    print(dado)
print()
print(f'O maior número digitado foi {maior}')
'''


from random import randint
from time import sleep

nomes = {}
dado = {}

cont = 1  # Contador inicia com 1, pois os FORs iniciam com 1
maior = 0
for c in range(1, 5):
    nomes[f'{c}'] = str(input(f'Digite nome do {c}° Jogador » ')).upper()

print('Colhendo os resultados dos Jogadores \n.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

for c in range(1, 5):
    dado[c] = randint(0, 6)
    if c == 0:
        maior = dado[c]
    else:
        if dado[c] > maior:
            maior = dado[c]

while cont <= len(dado):
    print(f'O jogador {nomes[f"{cont}"]} acertou o número {dado[cont]}')
# A chamada dos itens NOMES e DADO foram diferentes porque, apesar dos DADO e NOMES estarem em um dicionário, os índices
# dos NOMES foram gerados conforme o padrão das aspas simples ou duplas, enquanto que o DADO, quando gerou os números
# aleatórios, não foram colocados aspas em seus índices, por isso na hora da chamada foi sem as aspas.
    cont += 1

for k, v in dado.items():
    if v == maior:
        print(f'O Jogador {nomes[f"{k}"]} é o vencedor por acertar o número {v} considerado o maior. ')
