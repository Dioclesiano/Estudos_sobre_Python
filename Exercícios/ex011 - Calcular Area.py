# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta 2 metros quadrados.

largura = float(input('Digite a largura da parede que deseja pintar: '))
altura = float(input('Digite a altura da parede que deseja pintar: '))

print('A área a que irá pintar é {:.2f} m². Será necessário {:.2f} '
      'litros de tinta.'.format(largura*altura, (largura*altura)/2))
