
n = int(input('Digite um número para iniciar os 10 termos PA » '))
razao = int(input('Digite o número para representar a Razão da PA » '))
primeiro = n
cont = 1
acrescentar = 1
total = 10

while acrescentar != 0:
    total += acrescentar

    while cont <= total:
        print('{} - '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print(' < Pausa >\033[7;31m')
    print('\033[m*='*140)
    acrescentar = int(input('Digite [0] para sair ou quantos termos deseja acrescentar » '))
    print('*='*1400)
