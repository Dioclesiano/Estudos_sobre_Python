def real(valor, simbolo='R$'):
    return f'{simbolo}{valor:0.2f}'.replace('.', ',')


def formatar(msg):
    print('-_'*40)
    print(msg)
    print('_-'*40)


def notas(valor, cedulas):
    lista = [cedulas, 20, 10, 1]

    total = valor

    cont50 = cont20 = cont10 = cont1 = 0
    while total >= lista[0]:
        total -= lista[0]
        cont50 += 1

    while total >= lista[1]:
        total -= lista[1]
        cont20 += 1

    while total >= lista[2]:
        total -= lista[2]
        cont10 += 1

    while total >= lista[3]:
        total -= lista[3]
        cont1 += 1

    if cont50 > 0:
        print(f'Você receberá {cont50} nota(s) de {real(50)} Reais')
    if cont20 > 0:
        print(f'Você receberá {cont20} nota(s) de {real(20)} Reais')
    if cont10 > 0:
        print(f'Você receberá {cont10} nota(s) de {real(10)} Reais')
    if cont1 > 0:
        print(f'Você receberá {cont1} nota(s) de {real(1)} Real')
