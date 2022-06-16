#12) Faça um programa que leia um número é verifique se ele é um número primo.
cont = 0
n = int(input('Digite um número para saber se ele é primo: '))
aux = 1
while aux <= n:
    if n % aux == 0:
        print(f'\033[32m{aux}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{aux}\033[m', end=' ')
    aux += 1
if cont == 2:
    print(f'\nO número {n} é primo.')
else:
    print(f'\nO número {n} não é primo.')