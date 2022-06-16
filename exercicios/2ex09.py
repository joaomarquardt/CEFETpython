#9) Faça um programa que leia um número e diga se ele é ou não é múltiplo de 3.
n = int(input('Digite um número: '))
if n % 3 == 0:
    print(f'O número {n} é múltiplo de 3')
else:
    print(f'O número {n} não é múltiplo de 3')
