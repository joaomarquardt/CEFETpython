n = int(input('Digite um número: '))
print(f'Os primeiros {n} termos de um sequência de Fibonnacci são:')
c = 1
atras1 = atras2 = aux = num = 0
while c != n + 1:
    if c == 1:
        print(num, end=' > ')
    elif c == 2:
        num += 1
        print(num, end=' > ')
    elif c == 3:
        print(num, end=' > ')
        atras1 = 1
        atras2 = 0
    elif c > 3:
        aux = atras1
        atras1 = num
        atras2 = aux
        num = atras1 + atras2
        print(num, end=' > ')
    c += 1
print('FIM')

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55