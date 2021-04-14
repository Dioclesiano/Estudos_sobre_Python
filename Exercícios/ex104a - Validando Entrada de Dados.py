'''
Crie um programa que tenha a função LEIAINT(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex.:
n = leiaInt('Digite um n')
'''
def leiaint(numero):
    if numero.isnumeric():
        numero == int(numero)
        return f'é número inteiro {numero}'
    else:
        numero == str(numero)
        return f'não é um número inteiro'


n = str(input('Digite um número inteiro » '))

print(f'>> {n} << {leiaint(n)}')
