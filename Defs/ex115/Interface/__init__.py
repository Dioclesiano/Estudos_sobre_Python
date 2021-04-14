from ex113.Validador import leiaInt

def linha(tamanho=42):
    return '='*tamanho


def titulo(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    for k, v in enumerate(lista):
        print(f'  {k+1:<10}{v:>27}')
    print(linha())

    opcao = leiaInt('Digite sua Opção » ')  # Importei a DEF do exercício 113 que valida números inteiros
    return opcao
