'''
Faça um minisistema que utilize o INTERACTIVE HELP do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

Obs.: Use cores.
'''
def ajuda(comando, cor=0):
    print(cores[cor])
    help(comando)
    print(cores[cor])
    sleep(2)

def titulo(msg, cor=0):
    tamanho = len(msg) + 12
    print(cores[cor], end='')
    print('-'*tamanho)
    print(f'  <<< {msg} >>>')
    print('-'*tamanho)
    print(cores[0],end='')
    sleep(1)

# Programa Principal
from time import sleep

# Abaixo será criado uma lista com todas as cores do python. Esta lista é uma tupla pois os dados não serão alterados.
# Quando for fazer a chamada da cor, usarei apenas um número que corresponde a chave da lista.
cores = ('\033[m',           # Key 0 sem col
         '\033[0;30;41m',    # key 1 - Letra branca fundo vermelho
         '\033[0;30;42m',    # key 2 - Letra branca fundo verde
         '\033[0;30;43m',    # key 3 - Letra branca fundo amarelo
         '\033[0;30;44m',    # key 4 - Letra branca fundo azul
         '\033[0;30;46m',    # key 5 - Letra branca fundo roxo
         '\033[7;30m'        # key 6 - Letra preta fundo branco
         '')
# Quando passar o parâmtro, a melhor maneira de localizar a cor desejada será através de -> cores[cor]

while True:
    titulo('BUSCANDO FUNÇÃO OU BIBLIOTECA', 2)  # Título é uma DEF criada para personalizar os títulos
    comando = input('Digite a Função ou Biblioteca para obter ajuda » ').strip()

    if comando.upper() in 'FIM':
        break

    if comando.isnumeric():
        titulo('COMANDO INVÁLIDO! Número detectado', 3) # Neste print foi usado códigos de cores
                                                                          # contido em uma tupla que criei.
    else:
        ajuda(comando, 4) # Aqui está sendo chamada a DEF ajuda

titulo('ATÉ LOGO', 1)