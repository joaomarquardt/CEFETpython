#13) Faça um programa que leia um número e diga se ele está compreendido entre 20 e 90 ou não.
n = int(input('Digite um número: '))
if 20 <= n <= 90:
    print(f'O número {n} está compreendido entre 20 e 90')
else:
    print(f'O número {n} não está compreendido entre 20 e 90')
