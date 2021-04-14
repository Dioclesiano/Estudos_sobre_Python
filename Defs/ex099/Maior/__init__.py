from time import sleep


def maior(listas):
    for k, v in enumerate(listas):
        maior = 0
        print(f'Os números selecionados no {k+1}° sorteio foram >>> ', end='')
        for c in range(0, len(v)):
            sleep(0.5)
            print(f'{v[c]}', end='  ')
            if c == 0:
                maior = v[c]
            else:
                if v[c] > maior:
                    maior = v[c]
        sleep(0.5)
        print(f'o maior é {maior}')
