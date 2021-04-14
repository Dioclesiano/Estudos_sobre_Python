
def leiaFloat(msg):
    while True:
        try:
            n = input(msg)
            n2 = float(n)
        except ValueError:
            print(f'\033[31mEntrada Inválida\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m Operação Interrompida pelo Administrador.\033[m')
            break
        else:
            return f'{n2:0.2f}'.replace('.', ',')


def leiaString(msg):
    while True:
        try:
            simbolo = str(input(msg)).upper().strip()
            if not simbolo.isnumeric():
                simbolo = str(msg)
        except ValueError:
            print(f'\033[31mEntrada Inválida!\033[m')
        except (KeyboardInterrupt, NameError, AttributeError):
            print(f'\n\033[31mOperação interrompida pelo Administador. \033[m')
            print('Resultado Nulo')
            break
        else:
            return simbolo

def moeda(n, simbolo='R$'):
    return f'{simbolo}{n}'
