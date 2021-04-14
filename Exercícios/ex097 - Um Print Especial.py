'''
Faça um programa que tenha uma função chamada ESCREVA(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
'''
def escreva(msg):
    tamanho = len(msg) + 4

    print('~'*tamanho)
    print(' ', msg)
    print('~'*tamanho)


escreva('Surpreendentemente')
escreva('Eu sou um ótimo Programador')
escreva('Dioclesiano')