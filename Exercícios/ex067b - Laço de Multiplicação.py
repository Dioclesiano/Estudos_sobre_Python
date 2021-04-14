# Desafio feito pelo Professor

while True:
    n = int(input('Digite o número positivo para criar tabuada ou um número negativo para sair: '))
    if n < 0:
        print('Finalizado com sucesso.')
        break
    for c in range(1, 11):
        print(f'{n}  x {c:3} = {n*c:4}')
