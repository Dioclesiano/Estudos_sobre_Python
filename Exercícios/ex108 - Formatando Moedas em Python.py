'''
107 - Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça também um programa que importe esse módulo e use algumas dessas funções.

===> 108 - Adapte o código do DESAFIO 107, criando uma função adicional chamada REAL() que consiga mostrar os valores como um
valor monetário formatado.
'''
from ex108 import moedas

n = float(input('Digite o valor do Produto » '))
taxa = int(input('Digite a taxa » '))

print(f'O acréscimo de {taxa}% sobre {moedas.real(n)} corresponde a {moedas.real(moedas.aumentar(n, taxa))}')


'''
print(f'{moedas.real(moedas.dobro(n))} e {moedas.dobro(moedas.aumentar(n, 10))}')

neste exemplo, tenho o módulo moedas; o que vem depois do ponto é a função REAL criada para dar mostrar a quantidade 
monetária dos valores digitados. Quando eu abro os parênteses, significa que farei uso de outra DEF. Então eu utilizarei
a mesma estrutura. O primeiro código digitado será o Módulo, no caso MOEDAS, depois digito a função desejada.
'''
