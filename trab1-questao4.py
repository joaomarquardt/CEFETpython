'''4a Questão: Faça um programa que recebe um número inteiro no intervalo de 1 até 3000 e o escreva o seu
correspondente em algarismos romanos.'''

n = int(input('Digite um número entre 1 e 3000 para ser representado em algarísmos romanos: '))
M = D = C = L = X = IX = VIII = VII = VI = V = IV = III = II = I = 0
if 0 < n <= 3000:
    print(f'O número {n} em algarísmos romanos é: ', end='')
    if n >= 1000:
        M = n // 1000
        n = n % 1000
        print('M' * M, end='')
    if n % 1000 >= 900:
        print('CM', end='')
        n = n - 900
    if 500 <= n < 1000:
        D = n // 500
        n = n % 500
        print('D' * D, end='')
    if 400 <= n <= 499:
        print('CD', end='')
        n = n - 400
    if 100 <= n < 500:
        C = n // 100
        n = n % 100
        print('C' * C, end='')
    if 90 <= n <= 99:
        print('XC', end='')
        n = n - 90
    if 40 <= n <= 49:
        print('XL', end='')
        n = n - 40
    if 50 <= n < 100:
        L = n // 50
        n = n % 50
        print('L' * L, end='')
    if 10 <= n < 50:
        X = n // 10
        n = n % 10
        print('X' * X, end='')
    if n == 9:
        IX = n // 9
        print('IX', end='')
    if n == 8:
        VIII = n // 8
        print('VIII', end='')
    if n == 7:
        VII = n // 7
        print('VII', end='')
    if n == 6:
        VI = n // 6
        print('VI', end='')
    if n == 5:
        V = n // 5
        print('V', end='')
    if n == 4:
        IV = n // 4
        print('IV', end='')
    if n == 3:
        III = n // 3
        print('III', end='')
    if n == 2:
        II = n // 2
        print('II', end='')
    if n == 1:
        I = n // 1
        print('I')
else:
    print('Número inválido. Tente novamente.')
