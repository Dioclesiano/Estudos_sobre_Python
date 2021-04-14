def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha():
            print('ERRO')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor