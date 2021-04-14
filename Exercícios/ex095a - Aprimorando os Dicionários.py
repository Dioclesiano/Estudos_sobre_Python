# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.
# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador.

'''
jogador = {}
partida = []
time = []

while True:


    jogador['nome'] = str(input('Digite o nome do Jogador » '))

    jogos = int(input(f' >> Digite quantas partidas o(a) \033[1m{jogador["nome"].upper()}\033[m fez » '))

    partida.clear()
    for c in range(0, jogos):
        partida.append(int(input(f'  *** Digite quantos gols o(a) \033[1m{jogador["nome"].upper()}\033[m fez na partida {c+1} » ')))
    jogador['gols'] = partida[:]

    jogador['Total Gols'] = sum(partida)

    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] » ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S[Sim] ou N[Não] ')

    if resp == 'N':
        break

print()
print('-_'*60)
print()
print('CODIGO  ', end='')
for c in jogador.keys():
    print(f'{c.upper():20}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:3}     ', end='')
    for c in v.values():
        print(f'{str(c):20}', end='')
    print()
print()
print('-_'*60)

while True:
    busca = int(input('Digite o código do jogador ou [999 para Sair] » '))
    if busca == 999:
        break
    if busca >= len(time):
        print('     !!!ERRO!!!  O número digitado não corresponde à quantidade de jogadores cadastrados.')
    else:
        print(f'Você selecionou o jogador {time[busca]["nome"]}.')

        for k, v in enumerate(time[busca]['gols']):
            print(f'Na partida {k} o jogador {time[busca]["nome"]} fez {v} gols.')
    print()
'''

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []
jogador = {}
lista = []

while True:
    lista.clear()
    jogador['Nome'] = str(input('Digite o seu nome » ')).upper()
    quantidade = int(input(f'Digite a quantidade de partidas feita pelo jogador {jogador["Nome"]} » '))
    for c in range(0, quantidade):
        gol = int(input(f'Digite a quantidade de gols feitos por {jogador["Nome"]} na partida {c+1} » '))
        lista.append(gol)
    jogador['Gols'] = lista[:]
    jogador['Total'] = sum(lista)

    time.append(jogador.copy())

    while True:
        stop = str(input('Deseja continuar S[Sim] ou N[Não] » ')).upper()[0].strip()
        if stop in 'SN':
            break
        print('Entrada Inválida! Digite apenas S para Sim ou N para Não » ')
    if stop == 'N':
        break

print('*='*33)
for k in jogador.keys():
    print(f'{k:<30}', end='')
print()
print('*='*33)

for k, v in enumerate(time):
    for c in v.values():
        print(f'{str(c):<30}', end='')
    print()
print()

while True:
    print('=='*35)
    print('Pesquisa por Jogador ou Número:')
    localizar = input('Digite o J[Jogador], N[Número] ou S[Sair] » ')
    print('=='*35)

    if localizar.upper()[0] == 'S':
        print('Encerrando...')
        break

    elif localizar.upper()[0] == 'J':
        pesquisar = str(input('Digite o Nome do Jogador que deseja consultar » ')).upper().strip()
        for k, v in enumerate(time):
            for c in v.values():
                if v['Nome'] == pesquisar:
                    print(v)
                    break

    elif localizar.upper()[0] == 'N':
        pesquisar = int(input('Digite o número correspondente ao Jogador » '))
        for k, v in enumerate(time):
            if k+1 == pesquisar:
                for k in v.keys():
                    print(f'{k:<30}', end='')
                print()
                for c in v.values():
                    print(f'{str(c):<30}', end='')
                print()
                break
    else:
        print(f'\033[31mNão encontramos vínculos com "{localizar}". Tente novamente!\033[m')
