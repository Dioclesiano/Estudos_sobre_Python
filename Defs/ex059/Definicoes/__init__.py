def menu(* msg):
    for c in range(0, len(msg)):
        print(f'\033[31m Digite [{c+1}] para {msg[c]}\033[m')


def validarInteiro(numero):
    if numero.isnumeric() == False:
        print('\033[7;31m Entrada Inválida! Digite um código correspondente ao MENU\033[m ')
    else:
        return int(numero)


def somar(n1, n2):
    soma = n1 + n2
    return soma


def subtrair(n1, n2):
    sub = n1 - n2
    return sub


def multiplicar(n1, n2):
    mult = n1 * n2
    return mult


def dividir(n1, n2):
    menor = n1
    maior = n2
    if n2 < n1:
        menor = n2
        maior = n1

    div = maior / menor
    return div


def formatar(simbolos):
    return f'{simbolos:0.2f}'.replace('.', ',')
