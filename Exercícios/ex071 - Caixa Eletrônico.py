# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (números inteiros) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print('{:=^50}'.format(''))
print('{:^50}'.format(' NOTAS DE CAIXA DISPONÍVEL '))
print('{:^50}'.format('50€ 20€ 10€ e 1€'))
print('{:=^50}'.format(''))

valor = int(input('Digite o valor que deseja sacar » '))
total = valor

ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced  # O total menos o valor da célula
        totced += 1  # Contador
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break

# Usando Defs
# Nesta resolução com DEFs, será passado apenas o valor pedido pelo usuário e o valor maior da cédula.
from ex071.Saque import notas, formatar, real

valor = float(input('Digite o valor para Saque R$'))

formatar('')
notas(valor, 50)
formatar('')


# Usando todas as cédulas disponíveis => 100, 50, 20, 10, 5 e 1

saque = float(input('Digite o valor que deseja sacar » '))

valor = saque
nota = 100
quantidade = 0

while True:
    if valor >= nota:
        valor -= nota
        quantidade += 1
    else:
        if quantidade > 0:
            formatar(f'Será entregue {quantidade} notas de {real(nota)}')

        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1

        quantidade = 0
        if valor == 0:
            break
