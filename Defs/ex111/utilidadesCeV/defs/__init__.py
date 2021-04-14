def aumentar(n, aumento, simbolo, conversao=False):
    soma = n + (n * aumento)/100
    return int(soma) if conversao is False else moeda(soma, simbolo)


def descontar(n, diminuir, simbolo, conversao=False):
    dim = n - (n * diminuir)/100
    return int(dim) if conversao is False else moeda(dim, simbolo)


def moeda(n, simbolo):
    return f'{simbolo}{n:0.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, desconto=0, simbolo='R$', conversao=False):
    print()
    print('='*72)
    print(f'RESULTADO'.center(72))
    print('='*72)
    print(f'Aplicando {aumento}% sobre {moeda(n, simbolo)}, o total com juros é de      \t\t{aumentar(n, aumento, conversao)}')
    print(f'Aplicando {desconto}% sobre {moeda(n, simbolo)}, o total com desconto é de   \t\t{descontar(n, desconto, conversao)}')
    print('='*72)
