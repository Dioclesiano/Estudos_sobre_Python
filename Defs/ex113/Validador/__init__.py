#  Testador de Inteiro e Float
def leiaInt(dado):
    while True:
        try:
            num = int(input(dado))
        except(ValueError, TypeError):
            print('Comando Inválido! ', end='')
            continue
        except KeyboardInterrupt:
            print('\nFoi ativado a opção de cancelamento.')
            return 0
        else:
            return num


def leiaFloat(dado):
    while True:
        try:
            num = float(input(dado))
        except (ValueError, TypeError):
            print('Comando Inválido! ', end='')
        except KeyboardInterrupt:
            print('\nEncerrando o Programa!')
        else:
            return num