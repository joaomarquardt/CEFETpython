'''3a Questão: Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.
Ex.: Se n = 5
        *        *
        **      **
        ***    ***
        ****  ****
        **********
        ****  ****
        ***    ***
        **      **
        *        *
'''

n = int(input('\033[32;4;1mDigite um número:\033[m '))
c = 0
espaco = n
while c != n:
    c += 1
    espaco -= 1
    print('*' * c, end='')
    print(' ' * (espaco * 2), end='')
    print('*' * c)
while c != 1:
    c -= 1
    espaco += 1
    print('*' * c, end='')
    print(' ' * (espaco * 2), end='')
    print('*' * c)