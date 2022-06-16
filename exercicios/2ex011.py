#11) Faça um programa que leia um número e diga se ele é divisível por 3 e por 7.
# Obs.: utilize operador lógico.
n = int(input('Digite um número: '))
if n % 3 == 0 and n % 7 == 0:
    print(f'O número {n} é divisível por 3 e por 7')
else:
    print(f'O número {n} não é divisível por 3 e 7')