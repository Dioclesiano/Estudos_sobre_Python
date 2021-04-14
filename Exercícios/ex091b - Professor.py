# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem.
# Sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
# A importação do itemgetter consiste em exibir as chaves ou os valores, indicando suas posições

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

# Dicionário para exibir o ranking
ranking = dict()

# Função For para mostrar o resultado
for k, v in jogo.items():
    print(f'O {k} obteve o resultado » {v} « ')
    sleep(1)

# Esse comando coloca no ranking o menor valor para o maior
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Colocando o maior em primeiro lugar basta acrescentar o comando
# 'reverse=True' no código acima.

print(ranking)

# Tratando o resultado como Lista
print('=== Ranking dos Jogadores ===')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar » {v[0]} com {v[1]}')
    sleep(1)
