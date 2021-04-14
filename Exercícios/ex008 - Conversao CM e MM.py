# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

n = int(input('Digite um valor em Metros: '))

print('{} km'.format(n/1000))
print('{} hm'.format(n/100))
print('{} dam'.format(n/10))
print('{} dm'.format(n*10))

print('A metragem digitada corresponde a \n» {:.0f}'.format(n*100) + ' centímetros e » {:.0f}'.format(n*1000) +
      ' milímetros.')
