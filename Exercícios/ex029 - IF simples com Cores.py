# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite.

#  velocidade = int(input('Digite a velocidade do carro: '))

#  if velocidade >= 80:
#      print('Você foi multado!')
#      multa = (velocidade - 80)*7
#      print('Sua multa é de R$ {},00'.format(multa))
#  else:
#    print('Você não tem multa para pagar!')

# Acima meus exercícios, abaixo o professor fez

velocidade = float(input('Qual é a velocidade atual do carro? '))
print('tenha um bom dia! Dirija com segurança!')

#  Usando condição simples
if velocidade > 80:
    print('\033[30;41mMULTADO!\033[m \033[31mVocê excedeu o limite permitido que é de 80km/h.\033[m')
    multa = (velocidade - 80) * 7
    print('\033[40;31mVocê deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
