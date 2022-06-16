'''1a Questão: Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.
Ex.: Se n = 5
*
**
***
****
*****
****
***
**
* '''

n = int(input('Digite um número: '))
c = 0
while c != n:
    c += 1
    print('*' * c)
while c != 1:
    c -= 1
    print('*' * c)
