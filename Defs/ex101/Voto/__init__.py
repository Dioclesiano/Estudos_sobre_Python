from datetime import date


def voto(ano):
    atual = date.today().year  # Na variável ATUAL foi atribuído o comando do ano atual

    forma('Considerando que o voto é OBRIGATÓRIO para maiores de 18 anos, opcional dos 16 até 18 e desnecesário '
          'para menores de 16 anos')

    idade = atual - ano
    if idade < 16:
        print(f'Sua idade é {idade} anos e o ', end='')
        print(cor('VOTO NEGADO.', 1))

    elif 16 <= idade < 18:
        print(f'Sua idade é {idade} anos e o ', end='')
        print(cor('VOTO OPCIONAL.', 2))
    else:
        print(f'Sua idade é {idade} anos e o ', end='')
        print(cor('VOTO OBRIGATÓRIO.', 3))


def cor(msg, n):
    if n == 1:
        return f'\033[31m{msg}\033[m'
    elif n == 2:
        return f'\033[32m{msg}\033[m'
    elif n == 3:
        return f'\033[33m{msg}\033[m'


def forma(msg):
    tamanho = len(msg) + 4
    print('-'*tamanho)
    print(f' ', msg)
    print('-'*tamanho)
