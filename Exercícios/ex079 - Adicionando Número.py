'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.


lista = list()

while True:
    print('\033[35m*\033[m'*60)
    n = int(input('Digite um valor » '))
    print('\033[35m*\033[m'*60)


    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso')
    else:
        print('Número já foi adicionado')

    print('='*60)

    stop = str(input('\033[31m Digite [C] para continuar ou [S] para sair » \033[m')).strip().lower()
    if stop == 'c':
        pass
    elif stop == 's':
        print(lista)
        break
    else:
        print('\033[4mInformação incorreta. Tente novamente!\033[m')

'''

lista = []
listaordenada = []

contador = 0
stop = 'n'
while 's' not in stop:
    stop = input('Digite o número ou S para [Sair] » ')
    if stop.isalpha() == False:  # Este comando identifica os números e letras
        numero = float(stop)     # Aqui eu criei uma variável transformando uma string em float
        lista.append(f'{numero:0.2f}'.replace('.', ','))  # Com o replace eu substitui os pontos por vírgulas

# Abaixo o While dentre de um IF e outro While bloqueia os números que já foram digitados, ou seja, só aceita add
# na listaordenada apenas números que aindanão foram digitados.
        while numero not in listaordenada:
            
# A lógica deste IF abaixo é adicionar o primeiro número na listaordenada, deixando a condição que ele pode ser o maior
# ou o menor, isso será descoberto com mais eficiência após o segundo loop.
            if contador == 0 or numero > listaordenada[-1]:
                listaordenada.append(numero)
# Esse ELSE indica que os números que serão analisados estarão com o contador acima de zero, pois o contador igual a 
# Zero, é aceito no IF acima.
            else:
                cont = 0
# Com o contador definido, este While vai varrer toda a lista e verificar se o número é menor que o índice indicado pelo
# contador, se for menor será inserido, senão será executado pelo IF acima.
                while cont < len(listaordenada):
                    if numero <= listaordenada[cont]:
                        listaordenada.insert(cont, numero)
                        print(f'Número {numero} adicionado na posição {cont}')
                        break
                    cont += 1
    elif stop == 's':
        print()
        print(f'Os números digitados foram {lista}\nOs números permitidos foram {listaordenada}')
        print('FIM DO PROGRAMA')
    else:
        print(f'A palavra {stop.upper()} não foi identificada!')

    contador += 1
