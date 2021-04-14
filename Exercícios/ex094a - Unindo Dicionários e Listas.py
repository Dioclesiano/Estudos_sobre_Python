'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres cadastradas.
D) Uma lista com idade acima da média

pessoa = {}
lista = []
soma = media = 0
while True:             # Este é o While principal, que faz repetições até o usuário escrever 'N'.

    pessoa.clear()      # Para os dados não embolar, temos que limpar para que seja armazenado novos dados.
    pessoa['nome'] = str(input('Digite o seu nome » ')).capitalize()

    while True:         # Este While verifica se o usuário digitou as iniciais M ou F, senão emite msg de erro
        pessoa['sexo'] = str(input('Digite o seu sexo » ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M[Masculino] ou F[Feminino]')

    pessoa['idade'] = int(input('Digite a sua idade » '))
    soma += pessoa['idade']

    lista.append(pessoa.copy())     # Foi adicionado o dicionário na lista com uma cópia do dicionário

    while True:     # Este While verifica se o usuário digitou S ou N, senão emite uma msg de erro.
        resp = str(input('Deseja continuar? [S/N] » ')).upper()[0]
        if resp in "SN":
            break
        print('ERRO! Digite apenas S[Sim] ou N[Não]')

    if resp == 'N':     # Esta é a resposta para o while principal. Nesse ponto, se digitar N, sai do programa
        break

print()
print(f'=*'*30, 'RESPOSTAS', '*='*30)

print(f'Foram realizados \033[31m{len(lista)}\033[m cadastros. ')

media = soma / len(pessoa)
print(f'A soma das idades é de {soma:1.0f} anos e  média das idade é {media:1.0f} anos.')

print(f'As mulheres cadastradas foram -> ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end=' - ')
print()

print(f'As pessoas registradas com idade acima da média foram - ')
for c in lista:
    if c['idade'] >= media:
        for a, b in c.items():
            print(f' *** {a} = {b}')
'''

dado = {}
lista = []

somaIdade = 0
stop = 'S'
while stop not in 'N':
    dado['Nome'] = str(input('Digite seu nome » ')).upper()
    dado['Sexo'] = 'v'
    while dado['Sexo'] not in 'MF':
        dado['Sexo'] = str(input('Digite seu sexo M[Masculino] e F[Feminino] » ')).upper()[0].strip()

    dado['Idade'] = int(input('Digite sua idade » '))
    somaIdade += dado['Idade']

    lista.append(dado.copy())

    stop = 'V'
    while stop not in 'SN':
        stop = str(input('Deseja continuar S[Sim] N[Não] » ')).upper()[0].strip()

media = somaIdade / len(lista)

print(f' == NOME                 SEXO                 IDADE == ')
for k, v in enumerate(lista):
    print(f'{k+1} ', end=' ')
    for c in v:
        print(f'{v[c]:<22}', end=' ')
    print()

print('=-'*30)
print(f'Foram identificados {len(lista)} cadastros')
print(f'A média das idades >>> {media:0.0f} anos')
print('A(s) mulher(es) cadastrada(s) =>>> ', end=' ')
for k, v in enumerate(lista):
    for c in v:
        if c == 'Sexo' and v['Sexo'] == 'F':
            print(f'{v["Nome"]}', end=' - ')
print()
if dado['Idade'] > media:
    print(f'A(s) pessoa(s) com idade acima da média >>> ')
    for k, v in enumerate(lista):
        for c in v:
            if c == 'Idade' and v['Idade'] > media:
                print(f'    *** {v["Nome"]}  com  {v["Idade"]} anos')
