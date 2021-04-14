#  > > > Aqui será exibido o mesmo exercício de outra maneira
from ex109b.dinheiro import aumento, diminuir, real, formatando

n = float(input('Digite o valor do Produto » '))
taxa = int(input('Qual o valor da taxa » '))


while True:
    while True:
        dinheiro = str(input('Deseja a moeda formatada? S[Sim] ou N[Não] ')).strip().upper()[0]
        if dinheiro in 'SN':
            break
        print('Digite somente "S" para formatar moeda ou "N" para não formatar a moeda. ')

    if dinheiro == 'S':
        dinheiro = True
    if dinheiro == 'N':
        dinheiro = False

    escolha = str(input('Digite P[Parcelado] ou V[à Vista] » ')).strip().upper()[0]
    if escolha in 'PV':
        if escolha == 'P':
            formatando(f'O acréscimo de {taxa}% sobre {real(n, "R$")} corresponde a {aumento(n, taxa, dinheiro)}')
        if escolha == 'V':
            formatando(f'O desconto de {taxa}% sobre {real(n, "R$")} corresponde a {diminuir(n, taxa, dinheiro)}')

        break
    print('Digite somente "P" para compra Parcelado ou "V" para pagamento à Vista » ')
