'''
Crie um programa que tenha a função LEIAINT(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex.:
n = leiaInt('Digite um n')
'''
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


# Programa Principal
n = leiaInt('Digite um número Inteiro » ')
print(f'Você digitou o número inteiro {n}')
   