def moeda(a):
    return f'R${a:0.2f} reais'.replace('.', ',')


def real(n):
    num = moeda(n)
    return num


def ano(n):
    div = n * 12
    return div


def prestacao(a, b):
    div = a / b
    return div


def condicao(n):
    div = n - (n*30)/100
    return div


#def analise(salario, pre):