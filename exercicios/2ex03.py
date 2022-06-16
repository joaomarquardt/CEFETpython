#3) Faça um programa que leia um  número e diga se esse número é
# positivo, negativo ou nulo.
n = float(input('Digite um número: '))
if n > 0:
    print(f'O número {n} é positivo')
elif n < 0:
    print(f'O Número {n} é negativo')
else:
    print(f'O número {n} é nulo')