# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
# isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador » '))

print()
jogos = int(input(f'Digite quantos partidas o jogador \033[31m{jogador["nome"]}\033[m fez » '))

partidas = []

print()
for c in range(0, jogos):
    partidas.append(int(input(f'Digite quantos gols o jogador \033[4;31m{jogador["nome"]}\033[m fez na {c+1}ª partida » ')))

jogador['gols'] = partidas[:]

# A função SUM é uma simplificação para somar
jogador['total'] = sum(partidas)

print()
print('-='*30)
print(jogador)
print('-='*30)
print()

for k, v in jogador.items():
    print(f'O campo preenchido com »» {k} «« corresponde a »» {v} ««')

print()
print('- '*60)
print()

for i, v in enumerate(jogador['gols']):
    print(f'O jogador {jogador["nome"]} fez {v} gol(s) na {i+1}ª partida')

print()
print(f'O jogador {jogador["nome"]} fez o total de {jogador["total"]} gols. ')
