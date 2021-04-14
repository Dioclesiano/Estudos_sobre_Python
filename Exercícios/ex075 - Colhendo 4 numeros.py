'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

n = (int(input('Digite o primeiro número » ')),
    int(input('Digite o segundo número » ')),
    int(input('Digite o terceiro número » ')),
    int(input('Digite o quarto número » ')))

print()
print('='*50)
print(f'Os números digitados foram: \n\033[7;31m{n}\033[m')
print(f'O número 9 aparece {n.count(9)} vez(es).')

if 3 in n:
    print(f'O número 3 aparece pela primeira vez na {n.index(3)+1}ª posição.')
else:
    print('Não foi digitado o número 3.')

print(f'O(s) número(s) par(es) digitado(s) é(são) » ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end='  ')
print('')
print('='*50)
