# Faça um program que calcule a soma entre todos o números ímpares que são múltiplos de
# três e que se encontram no intervalo de 1 até 500.

s = 0
cont = 1
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  # Esse é um contador, pois soma +1
        s = s + c  # Esse é um Acumulador pois soma um valor
        print(c)
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
