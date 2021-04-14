'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados na tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time Criciúma.
'''
from ex069.Defs import formatar


times = ('Palmeiras', 'Corinthians', 'Flamengo', 'Cruzeiro', 'Santos', 'Grêmio', 'São paulo', 'Fluminense',
         'Vasco da gama', 'Internacional', 'Atlético mineiro', 'Bahia', 'Botafogo', 'Sport', 'Atlético paranaense',
         'Coritiba', 'Guarani', 'Criciúma', 'Juventude', 'Paulista')


for c in times:          # Se no FOR eu mandar printar 'Times', serão impressos a lista dos 20 times 20 vezes.
    print('\033[7;31m')  # Se no FOR eu mandar printar 'c', que é o contador, será impressos
    print(c)             # um time abaixo do outro.

print('\033[7m{:=^100}\033[m'.format(''))
print(f'\033[41mOs 5 times que estão na zona de classificação são: \n{times[:5]}')
print('\033[7m{:=^100}\033[m'.format(''))
print(f'\033[41mOs 4 times que estão na zona de desclassificação são: \n{times[-4:]}')
print('\033[7m{:=^100}\033[m'.format(''))
print(f'\033[41mOs 20 times brasileiros em ordem alfabética são: {sorted(times)}')
print('\033[7m{:=^100}\033[m'.format(''))
print(f'\033[41mO time "Criciúma" está na {times.index("Criciúma")+1}ª posição.')
print('\033[7m{:=^100}\033[m'.format(''))

ordenados = sorted(times)
formatar('  -_'*15)
print('EXIBIÇÃO DOS TIMES EM ORDEM ALFABÉTICA'.center(60))

for a in range(0, 1):
    print(ordenados[:4])
for b in range(0, 1):
    print(ordenados[5:9])
for c in range(0, 1):
    print(ordenados[10:14])
for d in range(0, 1):
    print(ordenados[15:20])
formatar('  _-'*15)
print()
formatar('  TABELA DE CLASSIFICAÇÃO')
for k, v in enumerate(times[:5]):
    print(f'\033[7;36m {k+1}º time classificado > {v} \033[m')
print()
formatar('  TABELA DE REBAIXAMENTO')
for k, v in enumerate(times[16:]):
    print(f'\033[7;31m {k+1}º time rebaixado > {v} \033[m')

print()
while True:
    try:
        opcao = str(input('Deseja pesquisar por colocação ou por nome » ')).upper().strip()
        if opcao in 'C' or opcao in 'COLOCAÇÃO' or opcao in 'COLOCACAO':
            while True:
                clube = int(input('Digite uma posição de 1 à 20 para saber a posição do time » '))
                if 1 <= clube <= 20 and clube <= 5:
                    print(f'O time na {clube}º posição é o {times[clube-1]} e está na zona de classificação.')
                    break
                elif 0 <= clube <= 20 and clube > 16:
                    print(f'O time na {clube}º posição é o {times[clube-1]} e está na zona de rebaixamento.')
                    break
                elif 5 < clube <= 16:
                    print(f'O time na {clube}º posição é o {times[clube-1]}.')
                    break
                else:
                    print(f'Sem dados para a {clube}º posição, pois está fora da lista de classificação.')
            break
        elif opcao in 'N' or opcao in 'NOME':
            while True:
                clube = str(input('Digite o nome do time » ')).capitalize().strip()
                if 0 <= times.index(clube) <= 5:
                    print(f'O {clube} está na lista de Classificados na {times.index(clube)+1}º posição.')
                    break
                elif 6 <= times.index(clube) < 16:
                    print(f'O {clube} está na {times.index(clube)+1}º posição.')
                    break
                elif 16 <= times.index(clube) <= 20:
                    print(f'O {clube} está na lista do rebaixamento na {times.index(clube)+1}º posição.')
                    break
        else:
            print('\033[31m  *  Entrada Inválida. Você precisa digitar C para [Colocação] ou N para [Nome] » \033[m')
    except ValueError:
        print('Você inseriu dados que não contém na Lista. Tente novamente.')
