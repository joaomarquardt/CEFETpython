#4) Faça um programa que imprima a raiz quadrada de um número caso ele seja positivo e o
# quadrado do número caso ele seja negativo.
n = int(input('Digite um número inteiro: '))
if n > 0:
    print(f'Raiz quadrada do número {n}: {n ** (1 / 2):.1f}')
elif n < 0:
    print(f'Quadrado do número {n}: {n ** 2:.1f}')
else:
    print(n)