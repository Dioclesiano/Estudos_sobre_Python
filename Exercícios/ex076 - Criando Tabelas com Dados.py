'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

* Nesse exercício eu iniciei o processo de formatação tabular, alinhando os dados
'''

print('='*50)

n = (str(input('Digite o nome do Produto » ')),
     float(input('Digite o preço do Produto » ')),

     str(input('Digite o nome do Produto » ')),
     float(input('Digite o preço do Produto » ')),

     str(input('Digite o nome do Produto » ')),
     float(input('Digite o preço do Produto » ')))

print()
print(f'Produto{"":>25}', 'Preço'.center(20))
print('='*50)
'''
for c in range(0, len(n)):
    if c % 2 == 0:
        print(f'{n[c]:-<30}', end='')
    else:
        print(f'{n[c]:->7.2f}')
'''
for c in range(0, len(n)):
     if c % 2 == 0:
          print(f'{n[c]:<40}', end='')
     else:
          print(f'{n[c]:>4.2f}')

