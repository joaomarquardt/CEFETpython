#10) Faça um programa que leia um número e diga se ele é ou não é divisível por 5.
n = int(input('Digite um número: '))
if n % 5 == 0:
    print(f'O número {n} é divisível por 5')
else:
    print(f'O número {n} não é divisível por 5')
