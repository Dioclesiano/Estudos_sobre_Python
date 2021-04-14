'''
Faça um programa que tenha uma função chamada FICHA(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s)')


nome = str(input('Digite o nome do Jogador » '))
gol = str(input(f'Digite quantos gol(s) o jogador {nome} fez » '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
