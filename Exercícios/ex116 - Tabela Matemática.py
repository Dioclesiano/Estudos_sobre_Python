'''
Colher dois números e reportar a tabela
'''

def operação(n1, simbol):

    if simbol == '+':
        for c in range(0, 10):
            print(f'{n1} + {c} = {n1+c}')
    elif simbol == '-':
        for c in range(0, 10):
            print(f'{n1} - {c} = {n1-c}')
    elif simbol == '*':
        for c in range(0, 10):
            print(f'{n1} * {c} = {n1*c}')
    else:
        for c in range(1, 11):
            print(f'{n1} : {c} = {n1/c:0.2f}')


n1 = int(input('Digite o primeiro número da tabela » '))

while True:
    simbol = input('Qual operação deseja fazer? ')
    if simbol in '+-*/':
        break
    print('Digite apenas [+ - * /] ')
    print('+[SOMA] -[SUBTRAÇÃO] *[MULTIPLICAÇÃO] e /[DIVISÃO] » ')


operação(n1, simbol)
