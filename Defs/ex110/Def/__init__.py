def aumentar(n, aumento, conversao=False):
    soma = n + (n * aumento)/100
    return int(soma) if conversao is False else moeda(soma)


def descontar(n, diminuir, conversao=False):
    dim = n - (n * diminuir)/100
    return int(dim) if conversao is False else moeda(dim)


def moeda(n, simbolo='R$'):
    return f'{simbolo}{n:0.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, desconto=0, conversao=False):
    print()
    print('='*72)
    print(f'RESULTADO'.center(72))
    print('='*72)
    print(f'Aplicando {aumento}% sobre {moeda(n)}, o total com juros é de      \t\t{aumentar(n, aumento, conversao)}')
    print(f'Aplicando {desconto}% sobre {moeda(n)}, o total com desconto é de   \t\t{descontar(n, desconto, conversao)}')
    print('='*72)
