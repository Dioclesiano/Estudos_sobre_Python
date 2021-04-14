# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.
# Regras para  esse exercício é que um lado deve ser menor que a soma dos outros dois lados.

print('-=-'*8)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*8)
print()
n1 = float(input('Digite o comprimento do lado do Triângulo » '))
n2 = float(input('Digite o comprimento do outro lado do Triângulo » '))
n3 = float(input('Digite o comprimento do último lado do Triângulo » '))
print()
if n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n1 + n2:
    print('='*60)
    print('Com os dados \033[32m{}, \033[33m{} e \033[34m{}\033[m \033[7;31;40mé '
          'possível montar um Triângulo.\033[m'.format(n1, n2, n3))
    print('='*60)
else:
    print('!'*64)
    print('Com os dados \033[35m{}, \033[36m{} e \033[37m{} \033[4;31mnão é possível montar um '
          'Triângulo\033[m.'.format(n1, n2, n3))
    print('!'*64)
