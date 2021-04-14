from moeda import aumentar, diminuir, dobro, metade

n1 = float(input('Digite o primeiro número » '))
print()

simbol = input('Digite a operação desejada '
               '\n[+] para somar unidades;'
               '\n[-] para diminuir unidades'
               '\n[*] para dobrar o valor digitado'
               '\n[/] para reduzir pela metade o valor digitado'

               '\n » ')

while True:
    if simbol == '+':
        n2 = float(input('Digite o segundo número » '))
        aumentar(n1, n2)
        break
    elif simbol == '-':
        n2 = float(input('Digite o segundo número » '))
        diminuir(n1, n2)
        break
    elif simbol == '*':
        dobro(n1)
        break
    elif simbol == '/':
        metade(n1)
        break
    else:
        print('Caracter Inválido! Reinicie o Sistema')
        break