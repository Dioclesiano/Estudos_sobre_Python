def resumo(n, credito, debito, brasao='R$', conversao=False):
    moeda(n, brasao)

    print('-'*60)
    print('RESULTADO'.center(60))
    print('-'*60)
    print(f'O juros de {credito}% sobre {aumentar(n, brasao)} corresponde a \t{aumentar(n, credito, brasao, conversao)}')
    print(f'O desconto de {debito}% sobre {moeda(n, brasao)} corresponde a \t{diminuir(n, debito, brasao, conversao)}')


def aumentar(n, credito, brasao, conversao=False):
    soma = n + (n * credito)/100
    return int(soma) if conversao is False else moeda(soma, brasao)


def diminuir(n, debito, brasao, conversao=False):
    sub = n - (n * debito)/100
    return int(sub) if conversao is False else moeda(sub, brasao)


def moeda(n, brasao):
    return f'{brasao}{n:0.2f}'.replace('.', ',')
