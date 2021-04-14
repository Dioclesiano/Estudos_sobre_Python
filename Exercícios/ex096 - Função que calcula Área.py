'''
Faça um programa que tenha uma função chamada ÁREA(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.

#Essa DEF foi definida no mesmo ambiente de desenvolvimento
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A largura {largura:5.2f}m e comprimento {comprimento:5.2f}m corresponde a uma área de {a:5.2f}m². ')


l = float(input('Digite a Largura do Terreno » '))
c = float(input('Digite o comprimento do Terreno » '))
area(l, c)

'''

# Esse código faz a chamada da DEF em outro local
from ex096.area import area
print('CONTROLE DE TERRENO'.center(30))
print('-'*30)
largura = float(input('Digite a Largura do terreno » '))
comprimento = float(input('Digite o comprimento do terreno » '))
area(largura, comprimento)