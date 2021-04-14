# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
time = list()
partidas = list()

while True:
    # O dicionário Jogador deve ser limpo para obter dados novos.
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador » '))

    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou » '))
    # A lista partidas deve ser limpa antes de iniciar nova leitura para não embaralhar os dados
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  * Quantos gols {jogador["nome"]} fez na {c + 1}ª partida » ')))

    print()
    # Cópia de lista adicionado ao Dicionário
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    # Cópia de dicionário adicionado à lista
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] » ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S[Sim] ou N[Não] ')

    if resp == 'N':
        break

print()
print('-='*30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [Digite 999 para Sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        novabusca = busca - 1
        print(f' -- Levantamento do Jogador {time[novabusca]["nome"]}: ')
        for i, g in enumerate(time[novabusca]['gols']):
            print(f'   No Jogo {i+1} fez {g} gols.')
        print('-'*40)
print('<< VOLTE SEMPRE >>')
