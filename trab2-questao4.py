'''4a Questão: Faça um programa que leia um número inteiro positivo e em seguida monte a figura abaixo. (Não utilize vetor)
Exemplo:
Se o número digitado for n=0. Deverá aparecer na tela:
*
Se o número digitado for n=1. Deverá aparecer na tela:
*
*
Se o número digitado for n=2. Deverá aparecer na tela:
**
*
*
Se o número digitado for n=3. Deverá aparecer na tela:
******
**
*
*
Se o número digitado for n=4. Deverá aparecer na tela:
************************
******
**
*
*
'''

from time import sleep
n = int(input('Digite um número: '))
while n < 0:
    print('Número inválido. Tente novamente.')
    sleep(1)
    n = int(input('Digite um número: '))
a = 0
b = i = c = 1
aux = fat = 0
while i <= n:
    aux = c
    c = a + b
    a = b
    b = c
    i += 1
i = 1
while i <= n:
    aux = b - a
    c = b
    b = a
    a = aux
    auxC = c
    fat = c
    while 1 < auxC:
        auxC -= 1
        fat *= auxC
    print('*' * fat)
    i += 1
print('*')