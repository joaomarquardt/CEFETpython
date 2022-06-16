'''3a Questão: Faça um programa que recebe um número inteiro no intervalo de 1 até 1 milhão e o escreva na tela por
extenso.'''

n = int(input('Digite um número entre 1 e 1 milhão: '))
num = n
if 0 < n <= 1000000:
    if n == 1000000:
        print('Um milhão')
    else:
        if 100000 <= n < 1000000:
            if 600000 <= n <= 999999 or 400000 <= n < 499999:
                if n // 100000 == 9:
                    print('Nove', end='')
                    n = n - 900000
                elif n // 100000 == 8:
                    print('Oito', end='')
                    n = n - 800000
                elif n // 100000 == 7:
                    print('Sete', end='')
                    n = n - 700000
                elif n // 100000 == 6:
                    print('Seis', end='')
                    n = n - 600000
                elif n // 100000 == 4:
                    print('Quatro', end='')
                    n = n - 400000
                print('centos', end=' ')
                if n % 100000 != 0:
                    print('e', end=' ')
            else:
                if 100000 <= n < 200000:
                    if 100000 <= n < 101000:
                        print('Cem', end=' ')
                        n = n - 100000
                    else:
                        print('Cento', end=' ')
                        n = n - 100000
                elif 200000 <= n < 300000:
                    print('Duzentos', end=' ')
                    n = n - 200000
                elif 300000 <= n < 400000:
                    print('Trezentos', end=' ')
                    n = n - 300000
                elif 500000 <= n < 600000:
                    print('Quinhentos', end=' ')
                    n = n - 500000
                if n % 100000 != 0:
                    print('e', end=' ')
        if 10000 <= n < 100000:
            if 10000 <= n < 20000:
                if 10000 <= n < 11000:
                    print('Dez', end=' ')
                    n = n - 10000
                elif 11000 <= n < 12000:
                    print('Onze', end=' ')
                    n = n - 11000
                elif 12000 <= n < 13000:
                    print('Doze', end=' ')
                    n = n - 12000
                elif 13000 <= n < 14000:
                    print('Treze', end=' ')
                    n = n - 13000
                elif 14000 <= n < 15000:
                    print('Catorze', end=' ')
                    n = n - 14000
                elif 15000 <= n < 16000:
                    print('Quinze', end=' ')
                    n = n - 15000
                elif 16000 <= n < 17000:
                    print('Dezesseis', end=' ')
                    n = n - 16000
                elif 17000 <= n < 18000:
                    print('Dezessete', end=' ')
                    n = n - 17000
                elif 18000 <= n < 19000:
                    print('Dezoito', end=' ')
                    n = n - 18000
                elif 19000 <= n < 20000:
                    print('Dezenove', end=' ')
                    n = n - 19000
            elif 20000 <= n < 30000:
                print('Vinte', end=' ')
                n = n - 20000
            elif 30000 <= n < 40000:
                print('Trinta', end=' ')
                n = n - 30000
            elif 40000 <= n < 50000:
                print('Quarenta', end=' ')
                n = n - 40000
            elif 50000 <= n < 60000:
                print('Cinquenta', end=' ')
                n = n - 50000
            elif 60000 <= n < 70000:
                print('Sessenta', end=' ')
                n = n - 60000
            elif 70000 <= n < 80000:
                print('Setenta', end=' ')
                n = n - 70000
            elif 80000 <= n < 90000:
                print('Oitenta', end=' ')
                n = n - 80000
            elif 90000 <= n < 100000:
                print('Noventa', end=' ')
                n = n - 90000
            if n // 1000 > 0:
                    print('e', end=' ')
        if 1000 <= n < 10000:
            if 1000 <= n < 2000:
                print('Um', end=' ')
                n = n - 1000
            elif 2000 <= n < 3000:
                print('Dois', end=' ')
                n = n - 2000
            elif 3000 <= n < 4000:
                print('Três', end=' ')
                n = n - 3000
            elif 4000 <= n < 5000:
                print('Quatro', end=' ')
                n = n - 4000
            elif 5000 <= n < 6000:
                print('Cinco', end=' ')
                n = n - 5000
            elif 6000 <= n < 7000:
                print('Seis', end=' ')
                n = n - 6000
            elif 7000 <= n < 8000:
                print('Sete', end=' ')
                n = n - 7000
            elif 8000 <= n < 9000:
                print('Oito', end=' ')
                n = n - 8000
            elif 9000 <= n < 10000:
                print('Nove', end=' ')
                n = n - 9000
        if num >= 1000:
            print('mil', end=' ')
            if 1 <= n < 101:
                print('e', end=' ')
        if 100 <= n < 1000:
            if 600 <= n <= 999 or 400 <= n < 499:
                if n // 100 == 9:
                    print('Nove', end='')
                    n = n - 900
                elif n // 100 == 8:
                    print('Oito', end='')
                    n = n - 800
                elif n // 100 == 7:
                    print('Sete', end='')
                    n = n - 700
                elif n // 100 == 6:
                    print('Seis', end='')
                    n = n - 600
                elif n // 100 == 4:
                    print('Quatro', end='')
                    n = n - 400
                print('centos', end=' ')
                if n % 100 != 0:
                    print('e', end=' ')
            else:
                if 100 <= n < 200:
                    if n == 100:
                        print('Cem', end=' ')
                        n = n - 100
                    else:
                        print('Cento', end=' ')
                        n = n - 100
                elif 200 <= n < 300:
                    print('Duzentos', end=' ')
                    n = n - 200
                elif 300 <= n < 400:
                    print('Trezentos', end=' ')
                    n = n - 300
                elif 500 <= n < 600:
                    print('Quinhentos', end=' ')
                    n = n - 500
                if n % 100 != 0:
                    print('e', end=' ')
        if 10 <= n < 100:
            if 10 <= n < 20:
                if n == 10:
                    print('Dez', end=' ')
                    n = n - 10
                elif n == 11:
                    print('Onze', end=' ')
                    n = n - 11
                elif n == 12:
                    print('Doze', end=' ')
                    n = n - 12
                elif n == 13:
                    print('Treze', end=' ')
                    n = n - 13
                elif n == 14:
                    print('Catorze', end=' ')
                    n = n - 14
                elif n == 15:
                    print('Quinze', end=' ')
                    n = n - 15
                elif n == 16:
                    print('Dezesseis', end=' ')
                    n = n - 16
                elif n == 17:
                    print('Dezessete', end=' ')
                    n = n - 17
                elif n == 18:
                    print('Dezoito', end=' ')
                    n = n - 18
                elif n == 19:
                    print('Dezenove', end=' ')
                    n = n - 19
            elif 20 <= n < 30:
                print('Vinte', end=' ')
                n = n - 20
            elif 30 <= n < 40:
                print('Trinta', end=' ')
                n = n - 30
            elif 40 <= n < 50:
                print('Quarenta', end=' ')
                n = n - 40
            elif 50 <= n < 60:
                print('Cinquenta', end=' ')
                n = n - 50
            elif 60 <= n < 70:
                print('Sessenta', end=' ')
                n = n - 60
            elif 70 <= n < 80:
                print('Setenta', end=' ')
                n = n - 70
            elif 80 <= n < 90:
                print('Oitenta', end=' ')
                n = n - 80
            elif 90 <= n < 100:
                print('Noventa', end=' ')
                n = n - 90
            if n % 10 > 0:
                print('e', end=' ')
        if 1 <= n < 10:
            if n == 1:
                print('Um', end=' ')
                n = n - 1
            elif n == 2:
                print('Dois', end=' ')
                n = n - 2
            elif n == 3:
                print('Três', end=' ')
                n = n - 3
            elif n == 4:
                print('Quatro', end=' ')
                n = n - 4
            elif n == 5:
                print('Cinco', end=' ')
                n = n - 5
            elif n == 6:
                print('Seis', end=' ')
                n = n - 6
            elif n == 7:
                print('Sete', end=' ')
                n = n - 7
            elif n == 8:
                print('Oito')
                n = n - 8
            elif n == 9:
                print('Nove', end=' ')
                n = n - 9
else:
    print('Número inválido. Tente novamente.')