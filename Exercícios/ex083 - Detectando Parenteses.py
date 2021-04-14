'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a a expressão passada está com os parênteses abertos e fechados na
ordem correta.
'''

expressao = str(input('Digite a expressão » '))
quantidade = []
for simbolo in expressao:
    if simbolo == '(':
        quantidade.append('(')
    elif simbolo == ')':
        if len(quantidade) > 0:
            quantidade.pop()
        else:
            quantidade.append(')')
            break

if len(quantidade) == 0:
    print('Esta expressão contém todos os parênteses!')
else:
    print(f'Esta expressão está faltando {len(quantidade)} parênteses!')
