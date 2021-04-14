'''
107 - Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça também um programa que importe esse módulo e use algumas dessas funções.

108 - Adapte o código do DESAFIO 107, criando uma função adicional chamada REAL() que consiga mostrar os valores como um
valor monetário formatado.

===> 109 - Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.
'''

from ex109a.dinheiro import *

preço = float(input('Digite o preço do produto » '))
taxa = int(input('Digite o percentual de Juros » '))
brasão = str(input('Digite o símbolo da moeda de seu país » ')).upper()

print()
print(f'O aumento de {taxa}% sobre {valor(preço, brasão)} equivale a {valor(aumentar(preço, taxa), brasão)}')
