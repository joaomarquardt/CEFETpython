"""
c = 55
b = 34
a = 21
aux = b - a
c = b
b = a
a = aux
"""
'''from time import sleep
n = int(input('Digite um número: '))
while n < 0:
    print('Número inválido. Tente novamente.')
    sleep(1)
    n = int(input('Digite um número: '))
c = 0
aux = 1
print('*')
while c != n:
    c += 1
    print('*' * aux * c)
    aux = aux * c'''
from time import sleep
n = int(input('Digite um número: '))
while n < 0:
    print('Número inválido. Tente novamente.')
    sleep(1)
    n = int(input('Digite um número: '))
c = n
a = b = auxB = 1
auxA = n
while a < n + 1:
    fat = 1
    while b < n:
        fat *= c
        c -= 1
        b += 1
    print('*' * fat)
    a += 1
    auxB += 1
    b = auxB
    auxA -= 1
    c = auxA
print('*')