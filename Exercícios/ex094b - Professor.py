# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade do grupo;
# C) Uma lista com todas as mulheres cadastradas.
# D) Uma lista com idade acima da média

pessoa = {}
galera = []

soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o seu nome » '))
    pessoa['sexo'] = str(input('Digite o seu sexo » ')).upper()[0]

    pessoa['idade'] = int(input('Digite a sua idade » '))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] » ')).upper()[0]
        if resp in 'SN':
            break
        print('Digite somente S[Sim] ou N[Não] » ')

    if resp == 'N':
        break

print()
print('*'*17)
print('* - RESPOSTAS - *')
print('*'*17)
print(f'RESPOSTA A - Localizamos »» {len(galera)} «« cadastros.')
print()

media = soma/len(galera)
print(f'RESPOSTA B - A média das idades cadastradas é {media:3.0f} anos.')
print()

print(f'RESPOSTA C - Localizado »» ', end='')
for c in galera:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print(' «« mulheres cadastradas.')
print()

print(f'RESPOSTA D - As pessoas com registro de idades acima da média foram » ')
for c in galera:
    if c['idade'] > media:
        print(f'    ** ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()

print()
print('Fim do Programa')
