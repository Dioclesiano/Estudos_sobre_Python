'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.


jogo = {}

jogo['nome'] = str(input('Digite o nome do Jogador » '))
jogo['partida'] = int(input('Digite a quantidade de partidas realizadas » '))

print()
jogo['soma'] = 0
for c in range(1, jogo['partida'] + 1):
    jogo['gols'] = int(input(f'Digite quantos gols feitos na {c}ª partida » '))
    jogo['soma'] += jogo['gols']

print()

print(f'O jogador {jogo["nome"]} fez {jogo["soma"]} gols durante o campeonato')

print()
print('-='*30)
print('Relatório')
print('-='*30)
for k, v in jogo.items():
    print(f'{k} é {v}')
'''

jogador = {}
lista = []

jogador['Jogador'] = str(input('Digite o nome do Jogador » ')).upper()
partidas = int(input(f'Digite quantas partidas o jogador {jogador["Jogador"]} participou » '))

soma = 0
for c in range(0, partidas):
    gol = int(input(f'     -- Digite quantos gols {jogador["Jogador"]} fez na {c+1}ª partida » '))
    lista.append(gol)
    soma += gol

jogador['Gols'] = lista
jogador['Total Gols'] = soma
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Jogador"]} jogou {partidas} partidas')
for k, v in enumerate(lista):
    print(f'    -- Na {k+1}ª partida {jogador["Jogador"]} fez {v} gol(s).')
print(f'Foi um total de {soma} gols')
