#15) Faça um programa que leia um número inteiro de 3 dígitos e informe se o algarismo da casa
# das centenas é par ou ímpar.
n = (input('Digite um número de 3 dígitos: '))
if len(n) != 3:
    print('O número digitado não tem 3 dígitos. Tente novamente.')
else:
    n = int(n)
    if (n // 100 ) % 2 == 0:
        print(f'O 1° dígito é par.')
    else:
        print(f'O 1° dígito não é par.')