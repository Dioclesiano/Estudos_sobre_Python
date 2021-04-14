from time import sleep

def formula(a, b, c):
    for cont in range(a, b, c):
        sleep(0.5)
        print(cont, end='  ')
    print()


def contagem(a, b, c):
    formula(a, b, c)
    if b < a:
        formula(a, b, -c)
