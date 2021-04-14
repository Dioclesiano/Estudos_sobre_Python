# Faça um programa que leia uma frase pelo teclado e mostre:
# * Quantas vezes aparece a letra 'A'
# * Em que posição ela aparece a primeira vez.
# * Em que posição ela aparece a última vez.

nome = str(input('Digite uma frase: ')).lower().strip()

print('Na frase digitada aparece a letra "A" » {} « vez (es).'.format(nome.count('a')))
print('A primeira aparição da letra "A" ocorre na » {}ª « posição.'.format(nome.find('a')+1))
print('A última aparição da letra "A" ocorre na » {}ª « posição.'.format(nome.rfind('a')+1))
